# If the employee is employed and their age is greater than 25, they get a bonus of 10% of their salary.
# If they are employed and their age is between 18 and 25 (inclusive), they get a bonus of 5% of their salary.
# If they are not employed, they do not get a bonus.

age = int(input("Enter your age:"))
salary = int(input("Enter your salary:"))
is_employed = input("Are you currently employed? (yes/no)")
is_employed = True if is_employed.lower() == "yes" else False 


if is_employed and age > 25:
    bonus = salary * 0.1
    print(f"Your bonus is: {bonus}")

if is_employed and age >= 18 or age <= 25 :
     bonus = salary * 0.05
     print(f"Your bonus is: {bonus}")
if not is_employed:
     bonus = 0
     print(f"Your bonus is: {bonus}")
else:
     print(f"Please fill in the required details and DON'T BE STUPID")

# this code is not perfect yet. 