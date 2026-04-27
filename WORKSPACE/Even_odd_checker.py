# Even odd checker
num = input("Enter any number:")
num = int(num)
even = num % 2       # The % sign is called the modulo operator and it only outputs the remainder.

if even == 0 :
    print("This is an even number")
else : 
    print("This is an odd number")

# modulo operator sign -- prints the remainder

print(15 % 4)   # output shuold be 3
print(20 % 6)   # output should be 2
print(400 % 5)  # output should be 0
