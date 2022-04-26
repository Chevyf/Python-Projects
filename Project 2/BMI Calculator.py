#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 
# ** can be used to determine the power for instance 2^3 = 2 ** 3
bmi = int(weight) / ( float(height) ** 2)

print (int(bmi))


# // is floor so transform float into int
# += -= *= /= takes the previous value and perform the action again 
#for ex +=  a = 2   a += 4  if you print it a will = 6