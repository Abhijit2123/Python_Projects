import random
import sys

print("Password Generator")
print("==========================")

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*123456789"

number = int(input("Please enter amount of passwords to generate: "))
if number == 0:
    sys.exit("\nPlease enter valid amount!!!")
    
length = int(input("Please enter password length: "))
if length == 0:
    sys.exit("\nPlease enter valid length!!!")
    
print("\nYour Passwords are: ")
for pwd in range(number):
    passwords = ''
    for i in range(length):
        passwords += random.choice(char)   # Takes random characters from the character string.
    
    print(passwords)
