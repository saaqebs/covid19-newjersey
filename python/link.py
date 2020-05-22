from datetime import date


url = 'https://www.nj.com/coronavirus/2020/{0}/where-is-the-coronavirus-in-nj-latest-map-update-on-county-by-county-cases-{1}.html'


def get_todays_date():
    '''Returns the current date along with the month number packaged in a tuple.

    Outputs: `current_date`: string, `month_number`: string 

    Example Output: ("march-25-2020", "03" )
    '''
    rn = date.today()
    month = rn.strftime("%B").lower()
    current_date = "{}-{}-{}".format(month, rn.day, rn.year)
    month_number = str(rn.month) if rn.month > 9 else '0' + str(rn.month)
    return current_date, month_number


def get_nj_dot_com_link(date, month, link=url):
    '''Returns the corresponding nj.com link given the `date` and `month`.

    Inputs: `date`: string, `month`: string

    Output: `link`: string

    Example: 
    "april-7-2020", "04" ->
    https://www.nj.com/coronavirus/2020/04/where-\
    is-the-coronavirus-in-nj-latest-map-update-on-county\
    -by-county-cases-april-7-2020".html
    '''
    print(url.format(month, date))
    return url.format(month, date)


def Link():
    date, month = get_todays_date()
    link = get_nj_dot_com_link(date, month)
    return link, date