#Write a program that works out whether if a given number is an odd or even number.
# % = modulo

number = int(input("Which number do you want to check? "))

x = number % 2
if x == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
