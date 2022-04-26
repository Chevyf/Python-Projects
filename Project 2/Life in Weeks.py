#Create a program using maths and f-Strings that tells us how many days weeks and months left
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.
# f string alows the program to print a string and automatically convert the other data types
#which must be entered in string using {}
# f must go infront of the "" or ' for ex f"hi {num}""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year = 90 - int(age)

x = 365 * year
y = 52 * year
z = 12 * year
print(f'You have {x} days, {y} weeks, and {z} months left.')