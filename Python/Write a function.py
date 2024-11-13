def is_leap(year):
    # Initialize a variable to store whether the year is a leap year or not
    leap = False

    # Check if the year is divisible by 4
    if (year % 4 == 0):
        leap = True  # Assume it's a leap year if divisible by 4
        
        # If the year is divisible by 100, it might not be a leap year
        if (year % 100 != 0):
            return leap  # It's a leap year if not divisible by 100
        
        else:
            # If the year is divisible by 400, it is a leap year
            if (year % 400 == 0):
                leap = True  # It's a leap year if divisible by 400
            else:
                leap = False  # Not a leap year if divisible by 100 but not by 400

    # Return whether the year is a leap year or not
    return leap

# Get the input year from the user
year = int(input())

# Print whether the given year is a leap year or not
print(is_leap(year))
