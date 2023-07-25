rows = int(input())
for i in range(1 , rows + 1):
    for j in range(i , rows):
        print(" " , end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i - 1):
        print("*", end=" ")
    print()
rows = rows - 1
for i in range(rows , 0 , -1):
    for j in range(rows,i-1,-1):
        print(" ", end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i-1):
        print("*",end=" ")
    print()