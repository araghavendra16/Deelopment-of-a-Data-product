import datetime
import wget
import datetime 
import pandas as pd 
import csv 

#three files to load 
#1. Confirmed cases 
confirmed ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

#2 Deaths 
deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

#3 Recovered 
recovered =  "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

#4 Stringent Index
stringentIndex = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv"


url = [confirmed, deaths, recovered, stringentIndex]


def scraper(url):
    
    # fetch data from multiple sources 
    
    """Johns Hopkins CSSE - epidemic data;
    Oxford COVID-19 Tracker - government responses.
    Data of interest per Date and Country/Region is as 
    follows."""
    data = [wget.download(urls) for urls in url]
    return data


scraper(url)


# Downloads epidemic data as CSV files to your folder