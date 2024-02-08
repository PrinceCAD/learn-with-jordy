from  random import *

def generate_weather_data(num_days):
    myArray = []
    try:
        for i in range(num_days):
            Days = {
                'day' : str(i+1).zfill(2) ,
                'temperature' : f"{randint(20, 40)} degrees",
                'humidity' : f"{randint(30, 90)}%"
            }
            myArray.append(Days)
    except TypeError:
        print("Please provide a valid number while calling the 'generate_weather_data' function....")
    return  myArray



def filter_data(weather_data, temp_threshold):
    filtered_data = []
    try:
        for i in weather_data:
            split_temp = i['temperature'].split()
            # Comparing data temperature to threshold
            if(int(split_temp[0]) >= temp_threshold):
                filtered_data.append(i)
    except TypeError:
        print("Please provide a valid weather dataset and a valid threshold while calling the 'filter_data' function....")
    return filtered_data




def calculate_average_humidity(weather_data):
    sum = 0
    count = 0
    try:
        for i in weather_data:
            split_humidity = i['humidity'].split('%')
            sum += int(split_humidity[0])
            count += 1
        average = sum/count
        # print(f"{average}%")
    except TypeError:
        return ("Please provide a valid weather dataset while calling the 'calculate_average_humidity' function....")
    return average
from  random import *





def sort_data_by_temperature(weather_data):
    sorted_data = []
    count = len(weather_data)

    for k in range(count):
        biggest_temp = 0
        try:
            for i in weather_data:
                split_temp = i['temperature'].split()
                if(int(split_temp[0])>biggest_temp):
                    biggest_temp = int(split_temp[0])
            for j in weather_data:
                split_temp = j['temperature'].split()
                if(int(split_temp[0]) == biggest_temp):
                    sorted_data.append(j)
                    weather_data.remove(j)
        except TypeError:
            return ("Please provide a valid weather dataset while calling the 'sort_data_by_temperature' function...")
    return sorted_data

