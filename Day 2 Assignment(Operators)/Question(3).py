#Python program to convert the temperature in degree centigrade to fahrenheit.

#Accept temperature in degree centigrade from user

celsius = float(input("Enter temperature in celsius:"))

#Conversion of celsius to fahrenheit
fahrenheit = (celsius * 9/5)+32

print(f"{celsius} degree celsius is equal to {fahrenheit} fahrenheit")