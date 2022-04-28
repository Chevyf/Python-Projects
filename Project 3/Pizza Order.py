print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

s = 15
m = 20 
l = 25

if size == 'S':
    s
    if add_pepperoni == 'Y':
        s += 2
    if extra_cheese == 'Y':
        s += 1
        print(f'Your final bill is: ${s}')
    else:
        print(f'Your final bill is: ${s}')

if size == 'M':
    m
    if add_pepperoni == 'Y':
        m += 3
    if extra_cheese == 'Y':
        m += 1
        print(f'Your final bill is: ${m}')
    else:
        print(f'Your final bill is: ${m}')

if size == 'L':
    l
    if add_pepperoni == 'Y':
        l += 3
    if extra_cheese == 'Y':
        l += 1
        print(f'Your final bill is: ${l}')
    else:
        print(f'Your final bill is: ${l}')
  
       

        


    

