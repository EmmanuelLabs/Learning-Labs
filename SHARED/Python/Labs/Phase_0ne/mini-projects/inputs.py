# Task 1: Interactive Profile
# Ask the user; name, age, and height
# Then print: Hello X, you are Y years old and Z meters tall.

name = input("Enter your name:")
age = input("Enter your age:")
age = int(age)
height = input("Enter your height:")
height = float(height)

print(f"Hello {name}, you are {age} years old and {height} meters tall.")

# Task 2: Simple calculator (user driven)
# Ask user for two numbers, then print sum, difference, product, & division

num1 = input("Enter your first number:")
num1 = int(num1)
num2 = input("Enter your second number:")
num2 = int(num2)

addition = num1 + num2
subtraction = num1 - num2
product = num1 * num2
division = num1 / num2

print(f"The sum of the two numbers is: {addition}")
print(f"The difference between the two numbers is: {subtraction}")
print(f"The product of the two numbers is: {product}")
print(f"The quotient of the two numbers is: {division:.3f}")

# Task 3: Even or Odd checker
# Ask user for a number then print whether it's even or odd

number = int(input("Enter a number:"))

if number % 2 == 0:
    print("This is an even number")
else:
    print("The number is odd")

# Task 4: Age in future
# Ask for current age, how many years into the future, then print future age.

current_age = input("Enter your current age:")
age = int(age)
future_years = input("How many years into the future?")
future_years = int(future_years)
future_age = age + future_years

print(f"In {future_years} years, you will be {future_age} years old.")

# Task 5: Basic Login system

username = input("Enter your username:")
password = input("Enter your password:")

if username == "admin" and password == "1234":
    print("Access granted")
else: 
    print("Access denied")

