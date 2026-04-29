# Task 1: Arithmetic Playground
# Ask user for two numbers and print: addition, subtraction, multiplication, division, floor division, modulus, exponent.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
mod = num1 % num2
exponent = num1 ** num2

print(f"The sum of the two numbers is: {addition}")
print(f"The difference between the two numbers is: {subtraction}")
print(f"The product of the two numbers is: {multiplication}")
print(f"The quotient of the two numbers is: {division}")
print(f"The rounded down integer value of the two numbers after dividing is: {floor_division}")
print(f"The remainder after dividing the two numbers is: {mod}")
print(f"The value of the first number raised to the second number is: {exponent}")

# Task 2: Comparison tester
# Ask user for two numbers and print results of: ==, !=, >, <, >=, <=.

first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

print(first_num == second_num)
print(first_num != second_num)
print(first_num > second_num)
print(first_num < second_num)
print(first_num >= second_num)
print(first_num <= second_num)

# Task 3: Eligibility checker
# Ask age, and has_id (yes/no -> convert to boolean)

age = int(input("Enter your age:"))
has_id = input("Do you have an ID? (yes/no)")
has_id = True if has_id.lower() == "yes" else False

if has_id is True and age >= 21:
    print("You are Eligible to enter")
else:
    print("You are NOT allowed to enter")

# Task 4: Number analyzer
# Ask user for a number and print; whether it is even or odd, whether it is positive, negative, or zero.

number = int(input("Enter any number:"))
remainder = number % 2

if remainder == 0:
    print("This is an even number")
else:
    print("This is an odd number")

if number > 0:
    print("This is a positive number")
elif number < 0:
    print("This is a negative number")
else:
    print("This is a zero")

# Task 5: Complex Decision system

user_age = int(input("Enter your age:"))
salary = int(input("Enter your salary:"))

if user_age < 21:
    print("Underage")
elif salary < 500:
    print("Low income")
else:
    print("Approved")





