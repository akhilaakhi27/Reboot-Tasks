def temperature_converter():
    temp = float(input("Enter temperature: "))
    unit = input("Convert to (Celsius or Fahrenheit): ").lower()
    
    if unit == "celsius":
        converted_temp = (temp - 32) * 5/9
        print(f"The temperature in Celsius is: {converted_temp}")
    elif unit == "fahrenheit":
        converted_temp = (temp * 9/5) + 32
        print(f"The temperature in Fahrenheit is: {converted_temp}")
    else:
        print("Invalid unit.")
temperature_converter()