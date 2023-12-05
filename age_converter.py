#!/usr/bin/env python3
# Program that converts age from years to days

# input for age, converts to integer
age_in_years = int(input("Enter your age in years "))

# converts years to days
age_in_days = age_in_years * 365

# minimum age validation
if age_in_years > 0:

    # outputs age in age_in_days
    print("Your age in days is roughly", age_in_days, "days old")

else:
    # if validation fails
    print("Sorry, you are too young to use this program")
