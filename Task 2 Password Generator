import string
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "()[]{},;:.-_/|\//~\\?+*=&^%$#@!><."

print("WELCOME TO THE PASSWORD GENERATOR\n")
length = int(input("Enter password length: "))

print(''' choose character set for password from these:
            1. uppercase letters
            2. Lowercase letters
            3. Digits
            4. Symbols
            5. Exit''')

password_list = ""
# Getting character set for password
while(True):
    choice = int(input("Pick a number "))
    if (choice == 1):

        # Adding uppercase letters to possible characters
        password_list += uppercase_letters
    elif (choice == 2):

        # Adding lowercase letter to possible characters
        password_list += lowercase_letters
    elif (choice == 3):

        # Adding digits to possible
        # characters
        password_list += digits
    elif (choice == 4):

        # Adding symbols to possible
        password_list += symbols
    elif (choice == 5):
        break
    else:
        print("Please pick a valid option!")
password = []
for i in range(length):
    # Picking a random character from our
    # character list
    char = random.choice(password_list)

    # appending a random character to password
    password.append(char)

    # printing password as a string
print("The random password is " + "".join(password))




