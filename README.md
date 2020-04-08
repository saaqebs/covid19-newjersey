# Coronavirus (COVID-19) Data in New Jersey
[
[ Township data from March 25, 2020 - Present](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/total_nj_covid19.csv?token=AIK7VXF6BA3HPELIM7D3F4K6RVZ66)  |  [Today's township data](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_covid19_today.json?token=AIK7VXB6O7QRBWLG4FALI626RV2C4) ]

This repository contains the latest up to date number of positive coronavirus cases there are in New Jersey. The data is counted by municipality, focusing the scope of the number of cases in New Jersey.

This data is collected and recorded by different counties in NJ, which is then compiled and posted in articles by [NJ.com](https://www.nj.com/coronavirus/). 

## Municipality Data from March 26, 2020 - Present

The data is stored in a CSV file format for an ongoing compilation of the number of cases per municipality in New Jersey. The structure of the file is as such:

| Date          | NJ Municipality | Number of Cases |
|---------------|-----------------|-----------------|
| march-25-2020 | allendale       | 4               |
| march-25-2020 | alpine          | 1               |
| ...           | ...             | ...             |

The "Date" column is structured as `{month name}-{day}-{year}`. The "NJ Municipality" variable contains the official municipality name as posted in [`nj_municipals.txt`](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_municipals.txt?token=AIK7VXHWPYTHBUSHNY2GIRS6RV55Y). The "Number of Cases" column is simply an integer indicating the number of cases.

## Municipality Data from Today

This data is collected everyday from nj.com and stored into a [JSON file](https://github.com/saaqebs/covid19-newjersey/edit/master/nj_covid19_today.json). The file structure is stored as such:

```json
{
    "last fetched": "april-7-2020",
    "data": {
        "allendale": 27, 
        "alpine": 15, 
        "bergenfield": 357,
        ...
    }
}

```

The file structure is much different from the cumulative data, but the variable names and structure remains the same. There are two variables inside of the JSON object: `last fetched` and `data`. 

The format of `last fetched` is `{month name}-{day}-{year}`. However, `data` is stored in a dictionary format where the key is the municipality name as prescribed from [`nj_municipals.txt`](https://raw.githubusercontent.com/saaqebs/covid19-newjersey/master/nj_municipals.txt?token=AIK7VXHWPYTHBUSHNY2GIRS6RV55Y) while the value is the number of positive cases in integer format.

## Additional Notes

Some counties have not been reporting the number of cases per township, creating a discord between other counties. As of April 6th, only Mercer County and Atlantic County have not posted their numbers while the rest have.

Most counties with high rates of infection have been posting daily, but other counties have been updating every few days.

Visit NJ.com/coronavirus for more information regarding COVID-19 in New Jersey.