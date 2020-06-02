import pandas as pd
import json, re

errors = json.load(open('./json/errors.json'))
substring_errs = errors[0]
fullstring_errs = errors[1]


def check_errors(town):
    for error in substring_errs.keys():
        town = town.replace(error,substring_errs[error])
        
    for error in fullstring_errs.keys():
        if town.strip() == error:
            return fullstring_errs[error]
    
    return town


def replace_town(row, county, visited_municipal):
    infected_township = re.split(':',row)
    town = check_errors(infected_township[0].strip()).strip()
    num_infected = int(re.findall(r'^\d+',infected_township[1].replace(',','').strip())[0])
    
    township = town + ' township'
    city = town + ' city'
    borough = town + ' borough'
    
    if town == 'address not reported' or town == 'no town' or town == 'unknown':
        return 'other', num_infected
        
    elif town in visited_municipal and visited_municipal[town] == False:
        visited_municipal[town] = True
        return town,num_infected
    
    elif township in visited_municipal and visited_municipal[township] == False:
        visited_municipal[township] = True
        return township,num_infected
    
    elif city in visited_municipal and visited_municipal[city] == False:
        visited_municipal[city] = True 
        return city, num_infected
    
    elif borough in visited_municipal and visited_municipal[borough] == False:
        visited_municipal[borough] = True 
        return borough, num_infected
    
    else: 
        print('ERROR TOWN NOT FOUND IN {}: {}'.format(county,town))
        return '',-1


def load_dataframe(data, covid_df, date, municipals):
    todays_data = []
    current_county = ''

    for row in data:
        if row in list(municipals.keys()):
            current_county = row
            continue

        if current_county == '':
            continue

        municipal, infected = replace_town(row, current_county, municipals[current_county])
        
        if municipal == '' or infected < 0:
            continue
        
        todays_data.append(
            pd.DataFrame(
                data=[[municipal,current_county,infected,date]],
                columns=['Municipal','County','Cases','Date']
            )
        )

    return covid_df.append(pd.concat(todays_data), ignore_index=True).copy()


def dataframe_to_json(df, counties):
    data = {}
    for county in counties:
        county_df = df[df['County'] == county]

        curr_county_data = {}
        for _, row in county_df.iterrows():
            curr_county_data[row['Municipal']] = row['Cases']

        data[county] = curr_county_data

    return data
        

def Clean(filepath, data, date, municipals):
    total_df = pd.read_csv(filepath)
    updated_df = load_dataframe(data, total_df, date, municipals)
    return updated_df


def Update(df, filepath):
    df.to_csv(filepath, mode='w', index=False)


def Today(df, date, counties, filepath):
    today_df = df[df['Date'] == date]
    today_json = {
        "last-fetched" : date,
        "data" : dataframe_to_json(today_df, counties)
    }
    with open(filepath, 'w') as datafile:
        json.dump(today_json,datafile)
    # today_df.to_json(filepath, orient='records')  
