# import csv
#
# with open("weather_data.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     # weather_data = list(csv_reader)
#     # print(weather_data)
#     temperatures = []
#     for row in csv_reader:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
#
# print(data_dict)
#
# temp_list = data["temp"].values.tolist()
# print(len(temp_list))
# print(temp_list)
#
# print(data["temp"].mean())
#
# #Get a column
# print(data["condition"])
# print(data.condition)

#Get data a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print((monday_temp * 9/5) + 32)

squirrel_data = pandas.read_csv("squirrel_data.csv")
# print(squirrel_data["Primary Fur Color"].unique())
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# Create a dataframe so that we can write into an output .csv file
# A DataFrame stores data as rows and columns, similar to a spreadsheet or SQL table.
# This makes relationships between values clear and easy to reason about.
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")









