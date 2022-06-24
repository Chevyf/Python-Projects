import random

# Picks a  random person out of the list to pay the bill

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

r = random.randint(0,int(len(names)-1))

print( names[r] + ' is going to buy the meal today!')
