def is_leap_year(year):
    # A year is a leap year if:
    # divisible by 4 AND (not divisible by 100 OR divisible by 400)
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year 🗓️")
else:
    print(f"{year} is not a leap year")