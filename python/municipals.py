from bs4 import BeautifulSoup
from urllib import request, error, parse

'''
## Getting All of New Jersey's Municipality Names

I grabbed and stored all of the New Jersey Municipality Names from this 
[Wikipedia Article](https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey)
and stored it in text file named `nj_municipals.txt`. 

This uses `urllib` to handle https request and grabbing the HTML file rendered 
by the Wikipedia article. It also uses `BeautifulSoup` to parse through the 
file to find specific targetted HTML tags necessary. 
'''


wiki_nj_municipalities_link = 'https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey'


def get_soup(link):
    '''
    This uses `urllib` to handle https request and grabbing the HTML file 
    rendered by the Wikipedia article. It also uses `BeautifulSoup` to parse 
    through the file to find specific targetted HTML tags necessary. 
    '''
    response = request.urlopen(link)
    nj_municipalities_html = response.read()
    soup = BeautifulSoup(nj_municipalities_html, 'lxml')
    return soup


def grab_municipal(row):
    return row.find_all('td')[1].text.strip().lower()


def get_municipals(soup):
    '''
    First, we grab each municipal name based on the table column. Then we 
    delete all the trailing whitespaces. Finally, we make every character 
    lowercase for string cleaning purposes.
    '''
    nj_municipal_rows = soup.find_all('tr')[1:566]
    nj_municipals = list(map(grab_municipal, nj_municipal_rows))
    return nj_municipals


def testing(nj_municipals):
    '''
    Testing that some municipalities are now in this Python list:
    '''
    assert 'south brunswick' in nj_municipals
    assert len(nj_municipals) == 565
    assert 'south toms river' in nj_municipals


def loading_to_text(nj_municipals):
    '''
    Creating and storing all of the municipalities into a text file called 
    `nj_municipals.txt`.
    '''
    new_file = open('../python/nj_municipals.txt', 'w+')
    for municipal in nj_municipals:
        new_file.write(municipal + '\n')
    new_file.close()


def __main__():
    soup = get_soup(wiki_nj_municipalities_link)
    municipals = get_municipals(soup)
    testing(municipals)
    loading_to_text(municipals)


if __name__ == "__main__":
    __main__()
