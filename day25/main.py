import pandas 

data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]


monday_temperature = (monday.temp*(5/9)) + 32

print(monday_temperature)
