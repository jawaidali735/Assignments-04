#Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
#There are 5 seconds in a year!
#You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.


DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60


#This solution is according to the question:
def main():
    year_in_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print(f"There are {year_in_seconds} seconds in a year!")

if __name__ == "__main__":
    main()




#Now this is what we can add some inputs.
#So if someone as about two, three manymore years in seconds

def years_in_seconds():

    user_input = float(input("Enter a number for years in seconds: "))
    year_in_seconds = (DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN ) * user_input


    if (user_input == 1 ):

        print(f"There are {year_in_seconds} seconds in {user_input} year!")
    else:
        print(f"There are {year_in_seconds} seconds in {user_input} years!")


if __name__ == "__main__":
    years_in_seconds()