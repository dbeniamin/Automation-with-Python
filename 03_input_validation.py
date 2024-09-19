# validate inputs with automation - uses pyinputplus lib
import pyinputplus as pyip

# creates an input and checks if the input is grater than or equal to 0
result_int = pyip.inputInt("Enter a random number:", min=0)


print(f"the random number is:{result_int}")


# a menu list can be generated and the choice can be further passed in another statement
result_menu = pyip.inputMenu(["blue", "yellow", "black"], lettered=True, numbered=False)

print(f"you chose a {result_menu} pen")

# validating input for email address
result_email = pyip.inputEmail("Please enter your email:")
print(f"the email address is: {result_email}")
