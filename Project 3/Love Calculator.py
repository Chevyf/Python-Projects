print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

a = name1.lower()
b = name2.lower()
t = int(a.count("t")) + int(b.count("t"))
r = int(a.count("r")) + int(b.count("r"))
u = int(a.count("u")) + int(b.count("u"))
e = int(a.count("e")) + int(b.count("e"))

l = int(a.count("l")) + int(b.count("l"))
o = int(a.count("o")) + int(b.count("o"))
v = int(a.count("v")) + int(b.count("v"))
e = int(a.count("e")) + int(b.count("e"))

true = t + r + u + e
love = l + o + v + e

love_score = int (str(true) + str(love))

if 10 > love_score or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 <= love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
