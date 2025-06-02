temp = int(input("Enter the temperature in Celsius: "))

if temp < 0:
    print("Freezing Cold ❄️")
elif 0 <= temp < 10:
    print("Very Cold 🥶")
elif 10 <= temp < 20:
    print("Cold 🧥")
elif 20 <= temp < 30:
    print("Pleasant ☁️")
elif 30 <= temp < 40:
    print("Hot 🔥")
else:
    print("Very Hot 🌞")