'''Write a program bu ysing strings
acccept the string from the user and perform all the operation'''


string = input("Enter a string:")

#Length of the string
length = len(string)
print("\nLength of the given string is:",length)

#Accessing the individual character
character = string[3]
print("\nAccessed character is:",character)

#Negative indexing
last_char = string[-1]
print("\nLast character of the string:",last_char)

#Slicing of the string
Substring = string[0:6]
print("\nSlicing portion of the string is:",Substring)

#Iterating over character
print("\nIteration of character:")
for char in string:
    print(char ,end=" ")

#Concatenation
string2 = input("\nEnter a new string for concatenation:")
result = string + " " +string2
print("New string after concatenation is:",result)

#Repetation of the string
num = int(input("\nEnter the number to repeate the string that number of times:"))
repeated_str = string * num
print("Repeated string: " , repeated_str)

#Membership of the string
sentence = input("\nEnter a sentence:")
check1 = input("Enter word that you want to check: ")
if check1 in sentence:
    print(f"{check1} is in the string")
else:
    print(f"{check1} is not in the string")

#String formatting
name = input("\nEnter name:")
age = int(input("Enter your age:"))
formatted_str = "Hello my name is %s, and I am %d years old."%(name,age)
print(formatted_str)

#Traversing the string
for char1 in string:
    print("\nTraversing the string using for loop:",char1)
        

    
        

