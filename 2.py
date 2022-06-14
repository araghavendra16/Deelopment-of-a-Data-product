import pandas as pd
import matplotlib.pyplot as plt

def clean_jhucdata(df):
  df1 = df.drop("Province/State", axis = 1)
  df1 = df1.drop("Lat", axis = 1)
  df1 = df1.drop("Long", axis = 1)
  df1 = df1.melt(['Country/Region'], var_name='Date', value_name='Confirmed')
  df1["Date"] = pd.to_datetime(df1["Date"])
  return df1

def clean_jhuddata(df):
  df1 = df.drop("Province/State", axis = 1)
  df1 = df1.drop("Lat", axis = 1)
  df1 = df1.drop("Long", axis = 1)
  df1 = df1.melt(['Country/Region'], var_name='Date', value_name='Deaths')
  df1["Date"] = pd.to_datetime(df1["Date"])
  return df1

def clean_jhurdata(df):
  df1 = df.drop("Province/State", axis = 1)
  df1 = df1.drop("Lat", axis = 1)
  df1 = df1.drop("Long", axis = 1)
  df1 = df1.melt(['Country/Region'], var_name='Date', value_name='Recovered')
  df1["Date"] = pd.to_datetime(df1["Date"])
  return df1

confirmed_cases_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
death_cases_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered_cases_df = pd.read_csv('time_series_covid19_recovered_global.csv')

confirmed_cases = clean_jhucdata(confirmed_cases_df)

death_cases = clean_jhuddata(death_cases_df)

recovered_cases = clean_jhurdata(recovered_cases_df)    


#a['Confirmed'].sum()                 
    
def merge_jhudata(df1, df2, df3):
  a = df1.merge(df2, how='left', on=['Country/Region', 'Date'])
  a = a.merge(df3, how='left', on=['Country/Region', 'Date'])
  return a

drc = merge_jhudata(confirmed_cases, death_cases, recovered_cases)

drc = drc.drop_duplicates(subset=['Country/Region','Date'], keep='first')
"""
def clean_oxforddata_si(data1):
  data1["Date"] = pd.to_datetime(data1["Date"], format='%Y%m%d')
  data1.drop(df.columns.difference(['CountryName','Date','StringencyIndex']), 1, inplace=True)
  data1.rename(columns = {'CountryName':'Country/Region'}, inplace = True)
  return data1

df = pd.read_csv('OxCGRT_latest.csv')
index_strI = clean_oxforddata_si(df)


view1 = drc.merge(index_strI, how='left', on=['Country/Region', 'Date'])

view1 = view1.drop_duplicates(subset=['Country/Region','Date'], keep='first')

view1.to_csv('view1.csv', index = False, encoding = 'utf-8')


# Running this file will generate csv file having attributes necessary for 1st view
# Epidemic data with Stringency Index. 
"""

