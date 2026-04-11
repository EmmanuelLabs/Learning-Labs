# Variables and Data Types
# Variables are used to store information that can be used later in the code.
#  They can hold different types of data, such as strings, integers, floats, and booleans.
# A variable is created by assigning a value to it using the equals sign (=).
#  The name of the variable should be descriptive and follow certain rules (e.g., it cannot start with a number, and it cannot contain spaces).

# Example of using variables to store information
x = 10  # This variable stores an integer value
y = 3.14  # This variable stores a float value
z = "Hello, World!"  # This variable stores a string value
is_true = True  # This variable stores a boolean value
print("Integer value:", x)
print("Float value:", y)
print("String value:", z)
print("Boolean value:", is_true)

# Guidelines for naming variables:
# 1. Use lowercase letters
# 2. Use underscores to separate words (e.g., my_variable)
# 3. Avoid using reserved keywords (e.g., if, else, while)
# 4. Make the variable name meaningful and descriptive of the data it holds (e.g., age, name, price)

# Python doesn't just store values. It stores the type of value as well.
# This is important because it helps the computer understand how to use the data. 
# For example, if you try to add a string and an integer, Python will give you an error because it doesn't know how to combine those two different types of data.
# The different data types in Python include:
# - Strings: Used to store text (e.g., "Hello, World!")
# - Integers: Used to store whole numbers (e.g., 10)
# - Floats: Used to store decimal numbers (e.g., 3.14)
# - Booleans: Used to store True or False values (e.g., True)
# Understanding variables and data types is fundamental to programming, as it allows you to store and manipulate data effectively in your code.

# Dynamic typing in python means that you can change the type of data stored in a variable without any issues. 
# For example, you can assign an integer value to a variable and later assign a string value to the same variable without any errors. 
# This flexibility allows for more dynamic and versatile coding styles. 
# However, it's important to be mindful of the data types you're working with to avoid unexpected behavior in your code.
# An example of dynamic typing in Python:
a = 30  # a is an integer
print("a is:", a)
a = "Now I'm text or a string!"  # a is now a string
print("a is:", a)

# Type checking is the process of verifying the type of data stored in a variable.
# You can use the built-in type() function to check the type of a variable in Python
# Example of type checking:
print(type(a))  # This will print <class 'str'> since a is currently a string
print(type(y))  # This will print <class 'float'> since y is currently a float
print(type(x))  # This will print <class 'int'> since x is currently an integer
print(type(is_true))  # This will print <class 'bool'> since is_true is currently a boolean

# Type conversion is the process of converting a value from one data type to another.
# You can use built-in functions like int(), float(), str(), and bool() to convert values between different data types in Python.
# Example of type conversion:
age = "25" # age is currently a string
print("Age:", age)
print("Type of age:", type(age))

# Convert the string to an integer
age = int(age)
print("Age:", age)
print("Type of age:", type(age))
# Convert the integer to a float
age = float(age)
print("Age:", age)
print("Type of age:", type(age))
# Convert the float to a string
age = str(age)
print("Age:", age)
print(type(age))

# In summary, variables are used to store information in a program, and data types define the kind of data that can be stored in those variables.
# Understanding how to use variables and data types effectively is crucial for writing efficient and error-free code