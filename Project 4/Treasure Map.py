

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

if row == 1:
    if column == 1:
        row1[0] = 'x'
    elif column == 2:
        row1[1] = 'x'
    elif column == 3:
        row1[2] = 'x'
elif row == 2:
    if column == 1:
        row2[0] = 'x'
    elif column == 2:
        row2[1] = 'x'
    elif column == 3:
        row2[2] = 'x'
elif row == 3:
    if column == 1:
        row3[0] = 'x'
    elif column == 2:
        row3[1] = 'x'
    elif column == 3:
        row3[2] = 'x'

print(f"{row1}\n{row2}\n{row3}")

# second solution

selecrow = map[row-1]
selecrow[column-1] = 'X'
print()
print(f"{row1}\n{row2}\n{row3}")