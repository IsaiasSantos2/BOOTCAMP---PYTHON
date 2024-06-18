import csv
with open("C:/Users/mundo/Desktop/BOOTCAMP - PYTHON/228. Reading CSV Data in Python/weather_data.csv") as data_file:
    data = csv.reader(data_file)
   # for row in data_file:
       # print(row)  
    
    temperatures = []
    for temp in data:
        temperatures.append(temp[1])
    print(temperatures)