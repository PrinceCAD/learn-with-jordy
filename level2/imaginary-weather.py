from  weatermodule import  *
def display(data):
    for i in data:
        print(i)
    return "done!"

weatherData = generate_weather_data(30)
display(weatherData)
threshold = input("\nEnter your desired bottom temperature limit : ")
try:
    threshold = int(threshold)
    weatherData = filter_data(weatherData, threshold)
    display(weatherData)

    humid = calculate_average_humidity(weatherData)
    print(f"\n Average Humidity : {humid}%\n")

    print(f" Sorted list --->\n")
    display(sort_data_by_temperature(weatherData))


except ValueError:
    print("Enter a valid integer temperature value")

