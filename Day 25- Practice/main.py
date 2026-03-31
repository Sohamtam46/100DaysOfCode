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

import pandas as pd
# data = pandas.read_csv("weather_data.csv")
#
# # average of the temperature
# temperature_data_avg = data["temp"].mean()
# print(f"Average Temp for week = {temperature_data_avg.round(2)}")
#
# # max temp in week
# temperature_data_max_value = data.temp.max()
# print(f"Max Temp for week = {temperature_data_max_value}")
#
# # get max temp row
# print(data[data.temp == data.temp.max()])
#
# # get monday temp in Fh
# monday = data[data.day == "Monday"]
# print((monday.temp*(9/5))+32)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260329.csv")

out_data = data["Primary Fur Color"].value_counts()
output = pd.DataFrame(out_data)
output.to_csv("Squirrel Color Count")

