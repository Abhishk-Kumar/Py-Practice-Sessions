import requests
from datetime import datetime, timedelta
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# hold dates in variables 
today_date=datetime.now()
weekago_date=today_date - timedelta(days=7)

# format dates according to api
start_date=weekago_date.strftime("%Y-%m-%d")
end_date=today_date.strftime("%Y-%m-%d")

api_url= f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response=requests.get(api_url)
data=response.json()
# print(json.dumps(data, indent=4))

# ____________________________________________


# extract dailydata
# creating a dataframe
# parse date into proper format to showcase in dataframe

daily_data=data['daily']

df=pd.DataFrame({
    'date':daily_data['time'],
    'max_temp':daily_data["temperature_2m_max"],
    'min_temp':daily_data["temperature_2m_min"]
})

# convert in right format
df['date']=pd.to_datetime(df['date'])

print(df)


# ---------------------------------

plt.figure(figsize=(10,6))
plt.plot(df['date'],df['max_temp'],marker="o", label="Max temp")
plt.plot(df['date'],df['min_temp'],marker="o", label="Min temp")

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather of past 7 days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather_chart.png')
plt.show()

# --------------------

# create data folder if not exist 

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/paris_weather.csv', index=False)
print("Finally data saved to csv file sucessfully")