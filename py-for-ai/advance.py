# import requests

# latitude=48.85
# longitude=2.35

# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# response=requests.get(url)
# data=response.json()



# # print(data.keys())
# temperature=data["current"]
# print(temperature)



import requests

def get_weather(latitude, longitude):
    api_url= f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response=requests.get(api_url)
    data=response.json()
    return data["current"]["temperature_2m"]

paris_temp=get_weather(48.85, 2.35)
tokyo_temp=get_weather(35.68, 139.69)
london_temp=get_weather(51.50, -0.12)

print(f"Currently Paris temperature is {paris_temp} °C")
print(f"Currently Tokyo temperature is {tokyo_temp} °C")
print(f"Currently London temperature is {london_temp} °C")


