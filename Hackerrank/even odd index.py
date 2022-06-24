#Given a string,S, of length N that is indexed from 0 to n-1 , print its even-indexed and odd-indexed characters as  
# 2 space-separated strings on a single line (see the Sample below for more detail).
# Note:  is considered to be an even index.
# Example s = adbecf
# Print abc def

n = int(input())
temp = []
for i in range (0,n):
    word = input()
    temp.append(word)

for i in range (0,n):
    for j in range (0, len(temp[i]), 2):
        print(temp[i][j], end='')
    print(end = ' ')
    for j in range (1, len(temp[i]), 2):
        print(temp[i][j], end='')
    print()

#solution 2
