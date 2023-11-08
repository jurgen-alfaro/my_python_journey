# used to check if two or more conditional statements are true

temperature = int(input("What is the temperature outside?: "))

if not (temperature >= 0 and temperature <= 30):
    print("The temperature is bad today!")
    print("Stay inside")
elif not(temperature < 0 or temperature > 30):
    print("The temperature is good today!")
    print("Go outside!")