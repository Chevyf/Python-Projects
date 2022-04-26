# Build program that calculates tip based on price and percentage

print('Welcome to the tip calculator')
billt = float(input('What was the total bill? '))
per = int(input('What percentage tip would you like to give? '))
split = int(input('How many people to split the bill? '))

total = billt + (billt * (per / 100) )

total /= split

result = round (total, 2)

print(f'Each person should pay: {result}')
