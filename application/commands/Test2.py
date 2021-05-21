import pandas as pd
import numpy as np
import glob
from datetime import datetime
from matplotlib import pyplot as plt
"""
x = [1,2,3]
y = [1,4,9]
plt.plot(x,y)
plt.show()
"""
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
#print(new_cases_df)
time = datetime.today().strftime('%d-%m-%Y')


def get_total_cases(time):
    df = pd.read_csv(path +time + ".csv")
    df = (df.loc[:, ['Country_Region', 'Confirmed']])
    
    us_data = df.loc[df['Country_Region'] == 'US', 'Confirmed'].sum()
    uk_data = df.loc[df['Country_Region'] == 'United Kingdom', 'Confirmed'].sum()
    india_data = df.loc[df['Country_Region'] == 'India', 'Confirmed'].sum()
    japan_data = df.loc[df['Country_Region'] == 'Japan', 'Confirmed'].sum()
    china_data = df.loc[df['Country_Region'] == 'China', 'Confirmed'].sum()
    canada_data = df.loc[df['Country_Region'] == 'Canada', 'Confirmed'].sum()
    france_data = df.loc[df['Country_Region'] == 'France', 'Confirmed'].sum()
    sweden_data = df.loc[df['Country_Region'] == 'Sweden', 'Confirmed'].sum()
    spain_data = df.loc[df['Country_Region'] == 'Spain', 'Confirmed'].sum()
    russia_data = df.loc[df['Country_Region'] == 'Russia', 'Confirmed'].sum()
    ukraine_data = df.loc[df['Country_Region'] == 'Ukraine', 'Confirmed'].sum()
    colombia_data = df.loc[df['Country_Region'] == 'Colombia', 'Confirmed'].sum()
    peru_data = df.loc[df['Country_Region'] == 'Peru', 'Confirmed'].sum()


    df = df.drop(index=df[df['Country_Region'] == 'US'].index)
    df = df.drop(index=df[df['Country_Region'] == 'United Kingdom'].index)
    df = df.drop(index=df[df['Country_Region'] == 'India'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Japan'].index)
    df = df.drop(index=df[df['Country_Region'] == 'China'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Canada'].index)
    df = df.drop(index=df[df['Country_Region'] == 'France'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Sweden'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Spain'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Russia'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Ukraine'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Colombia'].index)
    df = df.drop(index=df[df['Country_Region'] == 'Peru'].index)

    df = df.append({'Country_Region': 'US', 'Confirmed': us_data}, ignore_index= True)
    df = df.append({'Country_Region': 'United Kingdom', 'Confirmed': uk_data}, ignore_index= True)
    df = df.append({'Country_Region': 'India', 'Confirmed': india_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Japan', 'Confirmed': japan_data}, ignore_index= True)
    df = df.append({'Country_Region': 'China', 'Confirmed': china_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Canada', 'Confirmed': canada_data}, ignore_index= True)
    df = df.append({'Country_Region': 'France', 'Confirmed': france_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Sweden', 'Confirmed': sweden_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Spain', 'Confirmed': spain_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Russia', 'Confirmed': russia_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Ukraine', 'Confirmed': ukraine_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Colombia', 'Confirmed': colombia_data}, ignore_index= True)
    df = df.append({'Country_Region': 'Peru', 'Confirmed': peru_data}, ignore_index= True)

    df = df.sort_values("Confirmed")
    print(df)
    df.to_csv(r'testxd', header=None, index=None, sep=' ', mode='w')



def get_new_cases(day1,day2):
    df1 = pd.read_csv(path +day1+ ".csv")
    df2 = pd.read_csv(path + day2 + ".csv")
    gdf1 = (df1.loc[:, ['Country_Region', 'Confirmed', 'Deaths']])
    names = (df1.loc[:, ['Country_Region']])
    gdf2 = (df2.loc[:, ['Country_Region', 'Confirmed', 'Deaths']])


    gdf2.rename(columns = {'Confirmed' : 'Confirmed2'}, inplace = True)


    gdf3 = pd.concat([gdf1, gdf2], axis = 1)
    gdf4 = (df1.loc[:, ['Country_Region']])
    new_cases_df = gdf3["Confirmed"] - gdf2["Confirmed2"]
    new_cases_df = pd.concat([gdf4, new_cases_df], axis = 1)
    new_cases_df.rename(columns = {0: 'Cases'}, inplace = True)



    new_cases_df = new_cases_df.sort_values(by='Cases')

    us_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'US', 'Cases'].sum()
    uk_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'United Kingdom', 'Cases'].sum()
    india_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'India', 'Cases'].sum()
    japan_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Japan', 'Cases'].sum()
    china_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'China', 'Cases'].sum()
    canada_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Canada', 'Cases'].sum()
    france_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'France', 'Cases'].sum()
    sweden_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Sweden', 'Cases'].sum()
    spain_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Spain', 'Cases'].sum()
    russia_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Russia', 'Cases'].sum()
    ukraine_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Ukraine', 'Cases'].sum()
    colombia_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Colombia', 'Cases'].sum()
    peru_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Peru', 'Cases'].sum()
    brazil_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Brazil', 'Cases'].sum()
    germany_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Germany', 'Cases'].sum()
    mexico_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Mexico', 'Cases'].sum()
    chile_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Chile', 'Cases'].sum()
    italy_data = new_cases_df.loc[new_cases_df['Country_Region'] == 'Italy', 'Cases'].sum()


    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'US'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'United Kingdom'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'India'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Japan'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'China'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Canada'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'France'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Sweden'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Spain'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Russia'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Ukraine'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Colombia'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Peru'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Brazil'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Germany'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Mexico'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Chile'].index)
    new_cases_df = new_cases_df.drop(index=new_cases_df[new_cases_df['Country_Region'] == 'Italy'].index)

    new_cases_df = new_cases_df.append({'Country_Region': 'US', 'Cases': us_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'United Kingdom', 'Cases': uk_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'India', 'Cases': india_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Japan', 'Cases': japan_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'China', 'Cases': china_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Canada', 'Cases': canada_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'France', 'Cases': france_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Sweden', 'Cases': sweden_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Spain', 'Cases': spain_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Russia', 'Cases': russia_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Ukraine', 'Cases': ukraine_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Colombia', 'Cases': colombia_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Peru', 'Cases': peru_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Brazil', 'Cases': brazil_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Germany', 'Cases': germany_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Mexico', 'Cases': mexico_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Chile', 'Cases': chile_data}, ignore_index= True)
    new_cases_df = new_cases_df.append({'Country_Region': 'Italy', 'Cases': italy_data}, ignore_index= True)



    new_cases_df.dropna(subset = ["Cases", "Country_Region"], inplace=True)
    new_cases_df = new_cases_df.sort_values(by='Cases')
    """nan_value = float("NaN")
    new_cases_df.replace("", nan_value, inplace= True)
    new_cases_df.dropna(subset = ["Cases"], inplace=True)
    print(new_cases_df)"""
    print(new_cases_df)
    new_cases_df.to_csv(r'testxd2', header=None, index=None, sep=' ', mode='w')

    
    

def get_sweden_cases(day1):
    df1 = pd.read_csv(path +day1+ ".csv")
    df1 = (df1.loc[:, ['Province_State' ,'Country_Region', 'Confirmed']])

    df3 = df1.loc[df1["Country_Region"] == "Sweden", "Confirmed"]
    df3.columns = ['Confirmed', 'Province_State']
    print(df3)





    
    blekinge_data = df1.loc[df1["Province_State"] == "Blekinge", "Confirmed"]
    dalarna_data = df1.loc[df1["Province_State"] == "Dalarna", "Confirmed"]
    gavleborg_data  = df1.loc[df1["Province_State"] == "Gavleborg", "Confirmed"]
    gotland_data = df1.loc[df1["Province_State"] == "Gotland", "Confirmed"]
    halland_data = df1.loc[df1["Province_State"] == "Halland", "Confirmed"]
    jamtland_data = df1.loc[df1["Province_State"] == "Jamtland Harjedalen", "Confirmed"]
    jonkoping_data = df1.loc[df1["Province_State"] == "Jonkoping", "Confirmed"]
    kalmar_data = df1.loc[df1["Province_State"] == "Kalmar", "Confirmed"]
    kronoberg_data = df1.loc[df1["Province_State"] == "Kronoberg", "Confirmed"]
    norrbotten_data = df1.loc[df1["Province_State"] == "Norrbotten", "Confirmed"]
    orebro_data = df1.loc[df1["Province_State"] == "Orebro", "Confirmed"]
    ostergotland_data = df1.loc[df1["Province_State"] == "Ostergotland", "Confirmed"]
    skane_data = df1.loc[df1["Province_State"] == "Skane", "Confirmed"]
    stockholm_data = df1.loc[df1["Province_State"] == "Stockholm", "Confirmed"]
    uppsala_data = df1.loc[df1["Province_State"] == "Uppsala", "Confirmed"]
    varmland_data = df1.loc[df1["Province_State"] == "Varmland", "Confirmed"]
    vasterbotten_data = df1.loc[df1["Province_State"] == "Vasterbotten", "Confirmed"]
    vasternorrland_data = df1.loc[df1["Province_State"] == "Vasternorrland", "Confirmed"]
    vastmanland_data = df1.loc[df1["Province_State"] == "Vastmanland", "Confirmed"]
    vastragotaland_data = df1.loc[df1["Province_State"] == "Vastra Gotaland", "Confirmed"]

    plt.title("Cases in Swedens Regions")
    n_groups = 19
    index = np.arange(n_groups)
    bar_width = 0.10
    blek_rekt = plt.bar(0, blekinge_data, bar_width)
    dala_rekt = plt.bar(1, dalarna_data, bar_width)
    gavleborg_rekt = plt.bar(2, gavleborg_data, bar_width)
    gotland_rekt = plt.bar(3, gotland_data, bar_width)
    halland_rekt = plt.bar(4, halland_data, bar_width)
    jamtland_rekt = plt.bar(5, jamtland_data, bar_width)
    jonkoping_rekt = plt.bar(6, jonkoping_data, bar_width)
    kalmar_rekt = plt.bar(7, kalmar_data, bar_width)
    kronoberg_rekt = plt.bar(8, kronoberg_data, bar_width)
    norrbotten_rekt = plt.bar(9, norrbotten_data, bar_width)
    orebro_rekt = plt.bar(10, orebro_data, bar_width)
    ostergotland_rekt = plt.bar(11, ostergotland_data, bar_width)
    skane_rekt = plt.bar(12, skane_data, bar_width)
    stockholm_rekt = plt.bar(13, stockholm_data, bar_width)
    uppsala_rekt = plt.bar(14, uppsala_data, bar_width)
    varmland_rekt = plt.bar(15, varmland_data, bar_width)
    vasterbotten_rekt = plt.bar(16, vasterbotten_data, bar_width)
    vasternorrland_rekt = plt.bar(17, vasternorrland_data, bar_width)
    vastmanland_rekt = plt.bar(18, vastmanland_data, bar_width)
    vastragotaland_rekt = plt.bar(3, vastragotaland_data, bar_width)
    plt.xticks(index + bar_width, ('Ble', 'Dal', 'Gavl', 'Got', 'Hal','Jam','Jon','Kal','Kro','Nor','Ore','Skane','Stock','Upp','Varm','VB','VN','Vman','VGot'))
    plt.xlabel('Region')
    plt.ylabel('Cases')
    plt.tight_layout()
    plt.plot()
    plt.savefig('application/commands/static/sweden.png')

    
    
    

    """
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Blekinge'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Dalarna'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Gavleborg'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Gotland'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Halland'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Jamtland Harjedalen'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Jonkoping'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Kalmar'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Kronoberg'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Norrbotten'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Orebro'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Ostergotland'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Skane'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Stockholm'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Uppsala'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Varmland'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Vasterbotten'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Vasternorrland'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Vastmanland'].index)
    df2 = df1.drop(index=df1[df1['Province_State'] == 'Vastra Gotaland'].index)
    """
    """
    df3 = df3.append({'Province_State': 'Blekinge'}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Dalarna'}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Gavleborg'}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Gotland'}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Halland', 'Confirmed': halland_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Jamtland Harjedalen', 'Confirmed': jamtland_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Jonkoping', 'Confirmed': jonkoping_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Kalmar', 'Confirmed': kalmar_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Kronoberg', 'Confirmed': kronoberg_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Norrbotten', 'Confirmed': norrbotten_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Orebro', 'Confirmed': orebro_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Ostergotland', 'Confirmed': ostergotland_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Skane', 'Confirmed': skane_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Stockholm', 'Confirmed': stockholm_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Uppsala', 'Confirmed': uppsala_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Varmland', 'Confirmed': varmland_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Vasterbotten', 'Confirmed': vasterbotten_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Vasternorrland', 'Confirmed': vasternorrland_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Vastmanland', 'Confirmed': vastmanland_data}, ignore_index= True)
    df3 = df3.append({'Province_State': 'Vastra Gotland', 'Confirmed': vastragotaland_data}, ignore_index= True)
    """
    

    df1.to_csv(r'testxd3', header=None, index=None, sep=' ', mode='a')

def get_data():
    f = open("/home/pa1450/PA1450-2021/testxd", "r")
    split = f.readlines()
    
    return split


def get_data2():
    f = open("/home/pa1450/PA1450-2021/testxd2", "r")
    split = f.readlines()
    
    return split

def get_data3():
    f = open("/home/pa1450/PA1450-2021/testxd3", "r")
    split = f.readlines()
    
    return split





#print(gdf3.to_string)

#df3 = pd.concat([df1, df2])



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
