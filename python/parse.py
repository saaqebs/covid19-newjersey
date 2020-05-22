from urllib import request, error, parse
from bs4 import BeautifulSoup
import re


def get_article(url):
    '''Returns the important part (the article component) of the HTML as 
    a BeautifulSoup object given from the `url`. 

    Input: `url`: string

    Output: `articles`: BeautifulSoup object 
    '''
    response = request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    return soup.find_all('article')[0]


def parse_data(article, counties):
    ''' Returns a list of strings containing the raw text of each statistic 
    given from `artcle` which is a BeautifulSoup object.

    Input:
    `article`: BeautifulSoup object
    `counties`: string list

    Output:
    `data`: string list
    '''
    data = []
    print('PARSING ERRORS:')
    for row in article.find_all('p'):
        delims = '.+\:\s*\d*,?\d+'
        statistic = row.getText().lower()

        if ':' in statistic and '•' in statistic:
            cleaned_row = re.findall(delims, statistic)
            if len(cleaned_row) != 1:
                print(statistic)
            else:
                data.append(cleaned_row[0][1:].strip())

        for county in counties:
            if county in statistic:
                data.append(county)
                break

    print('...')
    return data


def Parse(link, counties):
    ''' Parses the COVID 19 data from the desired NJ.com `link` and assorts them
    based on the `counties` the municipalities reside in.

    Input:
    `link`: string
    `counties`: string list

    Output:
    `data`: string list
    '''
    article = get_article(link)
    data = parse_data(article, counties)
    return data
