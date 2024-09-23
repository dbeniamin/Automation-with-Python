# ERROR handling
# usually done by try / except blocks
# assert statement can be used as a debug tool

# testing the integer input and potential errors for non numbers or 0
# usage of try / except blocks
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}")
except ValueError:
    print("Enter a valid integer")
except ZeroDivisionError:
    print("You cannot divide by 0")

# usage of assertions for error handling

years = [1925, 1943, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
years.sort()  # start with .reverse()
print(years)
assert years[0] <= years[-1], "first element is greater than last element."
