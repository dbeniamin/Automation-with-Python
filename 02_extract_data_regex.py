# search , match and extract data with regex

import re

# create the regex you want to use. use .compile method
# \d - refers to a digit in regex
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d")

# test example for the regex compiler.
example = "the test number is 123-456-789"

result = phone_num_regex.search(example)

if result:
    print("Complete set of numbers:", result.group())
    # extracting the first 3 digits
    print("the first 3 group of digits is: ", result.group()[0:3])


