# ddp-project-araghavendra

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

The project is clearly explained in Development of Data products_project_document (1).pdf 

In the dashboard, I have created some new variables (it's called Measure in POWERBI). I use these measures extensively in visualizations. 
Since it's a timeseries dataset, I print the latest date's confirmed column as Total Confirmed. It's of simple logic. Same for deaths. 

If its not working, please write back to me immediately. 


