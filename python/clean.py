import pandas as pd
import json


nj_municipals = json.load(open('nj_municipals.json'))
counties = list(nj_municipals.keys())


def check_errors(town, fullstring_errs, substring_errs):
    for error in substring_errs.keys():
        town = town.replace(error,substring_errs[error])
        
    for error in fullstring_errs.keys():
        if town.strip() == error:
            return fullstring_errs[error]
    
    return town


def replace_town(row, county, visited_municipal):
    infected_township = re.split(':',row)
    town = check_errors(infected_township[0].strip()).strip()
    num_infected = int(re.findall('^\d+',infected_township[1].replace(',','').strip())[0])
    
    township = town + ' township'
    city = town + ' city'
    borough = town + ' borough'
    
    if town == 'address not reported' or town == 'unknown':
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


def load_dataframe(data, covid_df, date, municipals=nj_municipals):
    todays_data = []
    current_county = ''

    for row in data:
        if row in counties:
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


def clean(filepath, data, date):
    total_df = pd.read_csv(filepath)
    updated_df = load_dataframe(data, total_df, date)
    return updated_df

