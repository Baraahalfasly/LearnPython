import datetime

def has_friday_13(month, year):
    # Create a date object for the 13th of the given month and year
    date = datetime.date(year, month, 13)
    # Check if the day is Friday (4 represents Friday)
    return date.weekday() == 4

# Examples
print(has_friday_13(3, 2020))  # True
print(has_friday_13(10, 2017)) # True
print(has_friday_13(1, 1985))  # False
