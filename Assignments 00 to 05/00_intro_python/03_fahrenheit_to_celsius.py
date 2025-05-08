#Ans of Q3 in intro python.

# he Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)
 


def main():

    input_degrees_fahrenheit = float(input("Enter your Temperature:"))

    conversion_degrees_celsius = (input_degrees_fahrenheit - 32) * 5.0/9.0

    result = "\033[1;3m" + str(conversion_degrees_celsius) + "C"  + "\033[0m"

    # print(f"Temperature: {input_degrees_fahrenheit}F = {result}")
    print ("Temperature:" + " " +"\033[1;3m" + str(input_degrees_fahrenheit) + "F" + "\033[0m"  + " " + "=" + " " + result)

if __name__ == "__main__":
    main()

    