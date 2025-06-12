FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:  
    user_input = float(input("Enter the temperature to convert: "))
    specify = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if specify == 'C':
        result = convert_to_celsius(user_input)
        print(f"{user_input}°C is {result:.2f}°F")
    
    elif specify == "F":
        result = convert_to_fahrenheit(user_input)
        print(f"{user_input}°F is {result:.2f}°C")
    
    else:
        raise ValueError("Invalid input. Please specify 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")    



