Development of Data Products: 
This project main aim is building a POWERBI dashboard comprising the data about COVID-19. The data sources include: Oxford COVID-19 data, JOHN HOPKINS UNIVERSITY data from their respective websites. 
1st step we import the data using web scraping techniques, then we clean individual data, then we merge both data sources and import the data onto POWER BI. 
We build an interactive dashboard which enables users to view the information country-wise - death, recovered, overall death for a time period (with option to choose time period), overall recovered, etc.. 


instructions: 
Run 1.py 
This script downloads data sources necessary for the project.
It should download 4 csv files into your folder: 
a. time_series_covid19_recovered_global b. time_series_covid19_deaths_global c. time_series_covid19_confirmed_global d. OxCGRT_latest.csv

Run 2.py
This script prepares (clean, merge 2 different csv's) the data for dashboard visualizations. 
Please adjust the file location of csv files. 
The output is view1.csv. 

This file is already input in POWERBI file (dashboard130622.pbix)

In the dashboard, we have created some new variables (it's called Measure in POWERBI terminology). We use these measures extensively in visualizations. 
Since it's a timeseries dataset, we print the latest date's confirmed column as Total Confirmed. Same for deaths attribute. 

POWERBI dashboard:

![image](https://user-images.githubusercontent.com/61226849/216812236-336723b8-15b6-4d6c-bd97-59a06403ab07.png)
![image](https://user-images.githubusercontent.com/61226849/216812262-b2320918-b0f4-4901-bb2e-0b43542050d3.png)

