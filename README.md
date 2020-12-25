# Coronavirus (COVID-19) Data in New Jersey
[
[ Township data from March 25, 2020 - Present*](https://github.com/saaqebs/covid19-newjersey/blob/master/nj_total.csv) ([Raw CSV](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_total.csv))  |  [Today's township data](https://github.com/saaqebs/covid19-newjersey/blob/master/nj_today.json) ([Raw CSV](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_today.json)) ]

This repository contains the latest up to date number of positive coronavirus cases there are in New Jersey. The data is counted by municipality, focusing the scope of the number of cases in New Jersey.

This data is collected and recorded by different counties in NJ, which is then compiled and posted in articles by [NJ.com](https://www.nj.com/coronavirus/). 

*As of October 2020, NJ.com has not collected the data per township. Work is being done to find the data from another source.

## Municipality Data from March 26, 2020 - Present

The data is stored in a CSV file format for an ongoing compilation of the number of cases per municipality in New Jersey. The structure of the file is as such:

| Municipal | County        | Cases | Date          |
|-----------|---------------|-------|---------------|
| allendale | bergen county | 4     | march-25-2020 |
| alpine    | bergen county | 1     | march-25-2020 |
| ...       | ...           | ...   | ...           |

The "Date" column is structured as `{month name}-{day}-{year}`. The "Municipal" and "County" variable contains the official municipality name with its corresponding county as posted in [`nj_municipals.json`](./python/json/nj_municipals.json). The "Cases" column is simply an integer indicating the number of cases.

## Municipality Data from Today

This data is collected everyday from nj.com and stored into a [JSON file](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_today.json). The file structure is stored as such:

```json
{
    "last fetched": "april-7-2020",
    "data": {
        "bergen county" : {
            "allendale": 27, 
            "alpine": 15, 
            // ...
        },
        "essex county" : {
            // ...
        }
        // ...
    }
}

```

The file structure is much different from the cumulative data, but the variable names and structure remains the same. There are two variables inside of the JSON object: `last fetched` and `data`. 

The format of `last fetched` is `{month name}-{day}-{year}`. However, `data` is stored in a dictionary format where the key is a New Jersey county. The countyies then point to a dictionary containing the municipality name as prescribed from [`nj_municipals.txt`](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_municipals.txt)while the value is the number of positive cases in integer format.

## Data Publication Dates 
_Note: The sparse data publicaiton dates start from the summer 2020. Prior to July 2020, data was published daily._

| Month     | Dates                  |
|-----------|------------------------|
| July      | 1-4, 8, 16, 18, 23, 30 |
| August    | 1, 7, 13, 15, 20, 27   |
| September | 3, 10, 17, 24          |

## Additional Notes
_Note: The publication of this data has been discontinued on NJ.com's website._

As of April 26, 2020, all counties have been reporting township case numbers. However, some counties began disclosing the data earlier than other counties (eg. Atlantic and Mercer County), creating a discord in the data. 

There was no publication of data on 5/1/20 and 6/23/20. There was also no data published from 6/28/20 - 6/30/20 (3 days). 

Starting from July, NJ.com has been slowing down the daily publication of the data. Instead, they went with a sparse approach by providing an update every 5-8 days.

Starting from September 10th 2020, Somerset County combined Hillsborough Township and Millstone Township into one combined district for case reportings. The data is listed under Hillsborough from this date onwards.

Most (if not all) counties have been posting numbers daily, but other counties have been updating a variable amount of days.

Visit [this page](https://github.com/saaqebs/analytics-coronavirus-nj) for a brief article discussing some elementary analytics conducted on this dataset! 

Visit [NJ.com/coronavirus](https://www.nj.com/coronavirus/) for more information regarding COVID-19 in New Jersey.