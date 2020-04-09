import parse

json_file = '../nj_today.json'
csv_file = '../nj_total.csv'

sub_errors = {
    'parsippany': 'parsippany-troy hills',
    'south orange': 'south orange village',
    'pemberton boro': 'pemberton',
    'wantgage': 'wantage',
    'oldsman': 'oldmans',
    'bryram': 'byram',
    ' borough': '',
    ' city': ''
}

full_errors = {
    'peapack-gladstone': 'peapack and gladstone',
    'pepack-gladstone': 'peapack and gladstone',
    'clinton town': 'clinton township',
    'boonton town': 'boonton township',
    'hadonfield': 'haddonfield',
    'orange': 'city of orange',
    'peuannock': 'pequannock',
    'gutenberg': 'guttenberg',
    'rivervale': 'river vale',
    'highstown': 'hightstown',
    'pine hil': ' pine hill',
    'tewsbury': 'tewksbury',
    'hardick': 'hardwick',
}


def __main__():
    # getting the article's HTML
    date, month = parse.get_current_date()
    article_link = parse.get_nj_dot_com_link(date, month)
    article_soup = parse.get_html_from_link(article_link)

    # loading and cleaning the data
    data = parse.parse_data_from_html(article_soup)
    covid_data = parse.load_covid_data_into_dict(data, sub_errors, full_errors)

    # loading to the json and csv
    parse.load_to_json(json_file, date, covid_data)
    parse.load_to_csv(csv_file, date, covid_data)


if __name__ == "__main__":
    __main__()
