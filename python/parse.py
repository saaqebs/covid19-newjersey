from urllib import request, error, parse
from bs4 import BeautifulSoup
from datetime import date
import json
import csv
import re


nj_municipals = set(line.strip() for line in open('nj_municipals.txt'))


def get_current_date():
    '''Returns the current date along with the month number packaged in a tuple.

    Outputs: `current_date`: string, `month_number`: string 

    Example Output: ("march-25-2020", "03" )
    '''
    rn = date.today()
    month = rn.strftime("%B").lower()
    current_date = "{}-{}-{}".format(month, rn.day, rn.year)
    month_number = str(rn.month) if rn.month > 9 else '0' + str(rn.month)
    return current_date, month_number


def get_nj_dot_com_link(date, month):
    '''Returns the corresponding nj.com link given the `date` and `month`.

    Inputs: `date`: string, `month`: string

    Output: `link`: string

    Example: 
    "april-7-2020", "04" ->
    https://www.nj.com/coronavirus/2020/04/where-\
    is-the-coronavirus-in-nj-latest-map-update-on-county\
    -by-county-cases-april-7-2020".html
    '''
    return 'https://www.nj.com/coronavirus/2020/{0}/where-'\
        'is-the-coronavirus-in-nj-latest-map-update-on-county'\
        '-by-county-cases-{1}.html'.format(month, date)


def get_html_from_link(link):
    '''Returns the HTML as a BeautifulSoup object given from the `link`. 

    Input: `link`: string
    '''
    response = request.urlopen(link)
    html = response.read()
    return BeautifulSoup(html, 'lxml')


def parse_data_from_html(soup):
    ''' Returns a list of strings containing the raw text of each statistic 
    given from the BeautifulSoup object.

    Input:
    `soup`: BeautifulSoup object

    Output:
    `data`: string list
    '''
    article = soup.find_all('article')                 # article component
    data = []
    for row in article[0].find_all('p'):
        delims = '.+\:\s*\d*,?\d+'
        statistic = row.getText().lower()

        if '• springfield ' in statistic:
            statistic = statistic.replace('• springfield ', '• springfield: ')

        if ':' in statistic and '•' in statistic:      # how statistic is stored
            cleaned_row = re.findall(delims, statistic)
            if len(cleaned_row) != 1:
                print('ERROR IN LOADING STATS: {}'.format(statistic))
            else:
                data.append(cleaned_row[0][1:].strip())

    return data


def load_covid_data_into_dict(uncleaned_data, substring_errors, fullstring_errors):
    '''Cleans each row of the `uncleaned_data`, finds the corresponding township
    match based on `nj_municipals`, then stores it into a dictionary which is 
    then returned.

    Input: `uncleaned_data`: string list

    Output: `nj_covid_19_data`: dictionary {string : int}
    '''
    nj_covid_19_data = {}

    for row in uncleaned_data:
        infected_township = re.split(':', row)
        town = infected_township[0].strip()
        num_infected = int(infected_township[1].replace(',', '').strip())

        for error in substring_errors.keys():
            town = town.replace(error, substring_errors[error])

        for error in fullstring_errors.keys():
            if town.strip() == error:
                town = fullstring_errors[error]

        town = town.strip()
        township = town + ' township'
        city = town + ' city'

        if town in nj_municipals:
            nj_covid_19_data[town] = num_infected
        elif township in nj_municipals:
            nj_covid_19_data[township] = num_infected
        elif city in nj_municipals:
            nj_covid_19_data[city] = num_infected
        else:
            print('ERROR TOWN NOT FOUND IN NJ MUNICIPALS: {}'.format(town))

    return nj_covid_19_data


def load_to_json(filepath, date, covid_data):
    '''Loads the `date` and `covid_data` into the a specified JSON based on 
    the `filepath`.

    Input:
    `filepath`: string, 
    `date`: string, 
    `covid_data`: dictionary {string : int}
    '''
    json_data = {
        'last fetched': date,
        'data': covid_data
    }
    with open(filepath, 'w') as datafile:
        json.dump(json_data, datafile)


def load_to_csv(filepath, date, covid_data):
    '''Loads the `date` and `covid_data` into the a specified CSV based on 
    the `filepath`.

    Input:
    `filepath`: string, 
    `date`: string, 
    `covid_data`: dictionary {string : int}
    '''
    with open(filepath, 'a') as fulldf:
        for mun in covid_data:
            writer = csv.writer(fulldf)
            writer.writerow([date, mun, covid_data[mun]])
