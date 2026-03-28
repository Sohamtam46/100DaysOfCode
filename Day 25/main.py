# with open("./weather_data.csv","r") as data:
#     weather_data = data.readlines()


# import csv
# with open("./weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperature = []
#     for row in weather_data:
#         if not row[1] == "temp" :
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")

# average of the temperature
temperature_data_avg = data["temp"].mean()
print(f"Average Temp for week = {temperature_data_avg.round(2)}")

# max temp in week
temperature_data_max_value = data.temp.max()
print(f"Max Temp for week = {temperature_data_max_value}")

