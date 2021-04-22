import pandas as pd
import numpy as np
import glob

aggregated_data = []
path = "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"
all_files = glob.glob(path + "/*.csv")
for filename in all_files:
    aggregated_data.append(filename)

input1 = "11-05-2020.csv"#input("Skriv in datum för som du vill jämföra med nya cases ex (11-04-2020.csv)")
input2 = "11-04-2020.csv"#input("Skriv in datum för som du vill jämföra med nya cases ex (11-04-2020.csv)")

df1 = pd.read_csv(path +input1)
df2 = pd.read_csv(path + input2)
gdf1 = (df1.loc[:, ['Country_Region', 'Confirmed', 'Deaths']])
gdf2 = (df2.loc[:, ['Country_Region', 'Confirmed', 'Deaths']])
gdf2.rename(columns = {'Confirmed' : 'Confirmed2'}, inplace = True)


gdf3 = pd.concat([gdf1, gdf2], axis = 1)

new_cases_df = gdf3["Confirmed"] - gdf2["Confirmed2"]
print(new_cases_df)
print(gdf3)



#print(gdf3.to_string)

#df3 = pd.concat([df1, df2])


#print(df3.to_string())



#val1 = total_data.loc[total_data["Country_Region"] == "Sweden", "Confirmed"].values


#view ordered list of countries based on their total cases per capita
#view ordered list of countries based on their new cases per capita
#total_data = df.drop(['FIPS','Admin2','Province_State','Last_Update','Lat','Long_','Deaths','Recovered','Combined_Key','Case_Fatality_Ratio','Incident_Rate'], axis=1).head()


"""print(aggregated_data[-1])
lst = []
print(len(aggregated_data))
for x in aggregated_data:
    df = pd.read_csv(x)
    lst.append(df)
    
total_data = pd.concat(lst)"""
