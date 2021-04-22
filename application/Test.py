import pandas as pd
import numpy as np
import glob

aggregated_data = []
path = "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"
all_files = glob.glob(path + "/*.csv")
for filename in all_files:
    aggregated_data.append(filename)



print(len(aggregated_data))
for x in aggregated_data:
    df = pd.read_csv(x)
    total_data = pd.concat([df])




#view ordered list of countries based on their total cases per capita
#view ordered list of countries based on their new cases per capita
total_data = df.drop(['FIPS','Admin2','Province_State','Last_Update','Lat','Long_','Deaths','Recovered','Combined_Key','Case_Fatality_Ratio','Incident_Rate'], axis=1).head()
print(total_data.to_string())