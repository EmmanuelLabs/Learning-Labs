# Inputs and outputs
# Output is done with the print () function. 
print("Hello, World!")      # This prints an output to the console

# Input is done with the input() function.
name = input("What is your name? ")  # This prompts the user for input and stores it in the variable 'name'
print(f"Hello, {name}!")  # This prints a personalized greeting using the input from the user

# The output of the input() function is always a string. 
# If you want to get a different data type, you need to convert it.
age = input("How old are you? ")  # This gets the age as a string
age = int(age)  # This converts the age to an integer making it possible to perform numerical operations on it
print(f"You will be {age + 1} years next year") 
# This code takes the user's age, converts it to an integer, and then calculates what their age will be next year by adding 1 to it.

# Input + Different data types
# Integers
num1 = input("Enter your first number")
num1 = int(num1) # Convert the input to an integer

# Floats
num2 = input("Enter your second number")
num2 = float(num2) # Convert the input to a float

# Booleans
is_student = input("Are you a student? (yes/no) ")
is_student = True if is_student.lower() == "yes" else False

# String -- The default output
school = input("Enter your school name:")
print(f"Your school is: {school}")