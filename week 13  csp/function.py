def check_weather_temperature(temp: int):
   
    if temp >= 110 or temp <= -10:
        print("Extreme temperature warning!")
    elif temp >= -9 and temp <= 59:
        print("The weather is cold out")
    elif temp >= 60 and temp <= 89:
        print("The weather is warm out")
    elif temp >= 90 and temp <= 109:
        print("The weather is hot out")
    else:
        print("Temperature within normal range.")


temp = int(input("What is the weather today? "))
check_weather_temperature(temp)