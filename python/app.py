from clean import Clean, Update, Today
from link import Link
from parse import Parse

import pandas as pd
import sys, json

json_file = '../nj_today.json'
csv_file = '../nj_total.csv'


def __main__():
    nj_municipals = json.load(open('./json/nj_municipals.json'))
    counties = list(nj_municipals.keys())

    if len(sys.argv) == 1:
        url, date = Link()
    else: 
        url = sys.argv[1]
        date = sys.argv[2]
        print(url)
        print(date)
    
    data = Parse(url, counties)
    total_df = Clean(csv_file, data, date, nj_municipals)
    Update(total_df, csv_file)
    Today(total_df, date, json_file)



if __name__ == "__main__":
    __main__()
