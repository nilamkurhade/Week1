
from util.util_class import CelsiusToFahrenheit, FahrenheitToCelsius


def main():
    temp = int(input("Enter the temperature:"))
    print("Temprature in Fahrenheit: ", CelsiusToFahrenheit(temp))
    print("Temprature in celsius: ", FahrenheitToCelsius(temp))



if __name__ == "__main__":
    main()
# calculating Celsius To Fahrenheit temperature

