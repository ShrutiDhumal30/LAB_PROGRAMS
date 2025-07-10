#Declare two variables and print that which variable is largest using ternary operator.


#Accept two variables from the user.
num1 = int(input("Enter first variable:"))

num2 = int(input("Enter second variable:"))

#Using ternary operator to print largest variable.
result = num1 if (num1>num2) else num2

#print the largest variable
print("The largest number is:",result)

