#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
#on every year that is evenly divisible by 4
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

x = year % 4
y = year % 100
z = year % 400

if x == 0 and y == 0 and z == 0:
    print('Leap year.')
if x != 0:
    print('Not leap year.')
if x == 0 and y != 0 and z == 0:
    print('Leap year.')
if x == 0 and y == 0 and z != 0:
    print('Not Leap year.')
if x == 0 and y != 0 and z != 0:
    print('Leap year.')
