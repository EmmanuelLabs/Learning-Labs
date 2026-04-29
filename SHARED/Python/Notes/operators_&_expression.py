# Operators & expressions

# An operator is a symbol that performs a specific operation on one or more operands.
# An operand is a value that an operator acts upon.
# an example of an operand is a variable, a literal value, or the result of another expression.
# An expression is a combination of operators and operands that can be evaluated to produce a value.
# Examples of expressions:
# 5 + 3   # This is an expression that adds two numbers together. The operator is + and the operands are 5 and 3. The result of this expression is 8.
# a * b   # This is an expression that multiplies two variables together. The operator is * and the operands are a and b. The result of this expression will depend on the values of a and b.
# age > 18  # This is an expression that compares the value of the variable age to the number 18. The operator is > and the operands are age and 18. The result of this expression will be either True or False, depending on the value of age.

# Arithmetic operators:
# + (addition)
# - (subtraction)
# * (multiplication)
# / (division  - returns a float)
# // (floor division - returns an integer, that is, the largest integer less than or equal to the result of the division)
# % (modulus - returns the remainder of the division)
# ** (exponent - power, that is, a ** b means a raised to the power of b)

# Arithmetic operators are used to perform mathematical operations on numeric operands. They can be used with integers, floats, and other numeric types. The result of an arithmetic operation will depend on the types of the operands and the operator used.

# Examples:
a = 10
b = 3

print(a+b)   # Output: 13
print(a-b)   # Output: 7
print(a*b)   # Output: 30
print(a/b)   # Output: 3.3333333333333335
print(a//b)  # Output: 3
print(a%b)   # Output: 1
print(a**b)  # Output: 1000

# Comparison operators:
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

# Comparison operators return a boolean value (True or False) based on the comparison of the operands.
# for example, the expression age > 18 will return True if the value of age is greater than 18, and False otherwise.

# Examples:
age = 20

print(age == 18)  # Output: False
print(age > 18)   # Output: True
print(age < 18)   # Output: False
print(age != 18)  # Output: True
print(age >= 18)  # Output: True
print(age <= 18)  # Output: False

# Logical operators:
# and (logical AND)
# or (logical OR)
# not (logical NOT)

# Logical operators are used to combine multiple boolean expressions and return a boolean result, that is, True or False. 
# The and operator returns True if both operands are True. 
# The or operator returns True if at least one operand is True
# The not operator returns the opposite of the boolean value of its operand, for example, not True will return False, and not False will return True.

# Examples:

age = 20
is_student = True

print(age > 18 and is_student) # Output: True (both conditions are true)
print(age < 18 or is_student)  # Output: True (at least one condition is true)
print(not is_student)          # Output: False (is_student is True, so not is_student is False)

# Assignment operators (Not foundational, just shortcuts for common operations):
# = (assignment - assigns a value to a variable)
# += (add and assign - adds a value to a variable and assigns the result back to the variable)
# -= (subtract and assign - subtracts a value from a variable and assigns the result back to the variable)
# *= (multiply and assign - multiplies a variable by a value and assigns the result back to the variable)
# /= (divide and assign - divides a variable by a value and assigns the result back to the variable)
# %= (modulus and assign - calculates the modulus of a variable by a value and assigns the result back to the variable)
# **= (exponent and assign - raises a variable to the power of a value and assigns the result back to the variable)

# Assignment operators are used to assign values to variables and perform operations on them in a concise way. 
# They allow you to update the value of a variable based on its current value without having to write the variable name multiple times.

# Examples:

x = 10
x += 5  # This is equivalent to x = x + 5
print(x) # Output: 15

x **= 4  # This is equivalent to x = x ** 4, which in this case x is 15, so it will calculate 15 raised to the power of 4
print(x)  # Output: 50625 (15 raised to the power of 4 is 50625)

name = "Intuitive"
name += " Dialect" # This is equivalent to name = name + " Dialect"

print(name) # Output: "Intuitive Dialect"
print(name * 3) # Output: "Intuitive DialectIntuitive DialectIntuitive Dialect" (the string is repeated 3 times)

say = "Hello"
say += " World" 
print(say)

# Order of operations (PEMDAS/BODMAS):
# In Python, the order of operations (also known as operator precedence) determines the sequence in which operators are evaluated in an expression.
# The order of operations in Python is as follows:
# 1. Parentheses ( )
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor Division //, Modulus %
# 4. Addition +, Subtraction -
# 5. Comparison operators (==, !=, >, <, >=, <=)
# 6. Logical operators (not, and, or)

# When evaluating an expression, Python will first evaluate any expressions within parentheses, then perform exponentiation, followed by multiplication, division, floor division, and modulus, then addition and subtraction, followed by comparison operators, and finally logical operators.
# What if there are multiple operators with the same precedence? In that case, Python evaluates them from left to right. For example, in the expression 10 - 5 + 2, both the subtraction and addition operators have the same precedence, so Python will evaluate them from left to right, resulting in (10 - 5) + 2 = 5 + 2 = 7.
# Will the same apply if we have multiplication, division, and maybe modulus in the same expression? Yes, in that case, Python will also evaluate them from left to right. For example, in the expression 10 * 5 / 2, both the multiplication and division operators have the same precedence, so Python will evaluate them from left to right, resulting in (10 * 5) / 2 = 50 / 2 = 25.

# Examples:
result = 10 + 5 * 2
print(result) # Output: 20 (multiplication is performed before addition)

# Combining everything (Real Expression thinking):
age = 22
salary = 500
is_employed = True
# Let's say we want to calculate a bonus based on the following criteria:
# If the employee is employed and their age is greater than 25, they get a bonus of 10% of their salary. 
# If they are employed and their age is between 18 and 25 (inclusive), they get a bonus of 5% of their salary. 
# If they are not employed, they do not get a bonus.




