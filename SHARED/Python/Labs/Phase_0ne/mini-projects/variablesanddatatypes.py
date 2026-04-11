# Mini-lab 2: Variables and Data Types
# Task 1: Personal profile system
# Create variables to store your name, age, height, and whether you are a student, then print them in a sentence.

name = "Intuitive Dialect"
age = 22
height = 5.7 # in feet
is_student = True
print(f"My name is {name}, I am {age} years old, {height} feet tall, and it is {is_student} that I am a student.") 

# Task 2: Simple math system
# Create: variables to store two numbers, then perform and print the results of addition, subtraction, multiplication, and division.
a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a/b

print(f"The sum of {a} and {b} is: {addition}")
print(f"The difference between {a} and {b} is: {subtraction}")
print(f"The product of {a} and {b} is: {multiplication}")
print(f"The quotient of {a} divided by {b} is: {division}")

# Task 3: Type checker
# Create variables of each type and print their types using the type() function.
title = "Network Engineer"
print("I am a", title)
print("The variable 'title' is of type: ", type(title))

salary = 500
print("My salary is: ", salary, "dollars per hour")
print(f"The variable 'salary' is of type: {type(salary)}")

experience = 4.5
print(f"I have {experience} years of experience in the field.")
print(f"The variable 'experience' is of type: {type(experience)}")

is_employed = True
print(f"Am I currently employed? {is_employed}")
print(f"The variable 'is_employed' is of type: {type(is_employed)}")

# Task 4: Type conversion trap
# Create two variables, both strings that represent numbers, and try to add them together.
# Don't use sum as a variable name since it's a built-in function in Python.
num1 = "10"
num2 = "5"
total = num1 + num2
print("result of adding ", num1, "and", num2, "as strings is:", total)
# Now converting the strings to integers first and then add them together
num1 = int(num1)
num2 = int(num2)
total = num1 + num2
print(f"result of adding {num1} and {num2} as integers is: {total}")