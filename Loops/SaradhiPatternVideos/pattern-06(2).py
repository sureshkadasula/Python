'''
'''
rows = int(input("Enter row count : "))
p=rows
for i in range(rows,0,-1):
    for j in range(rows ,i,-1):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    print()
    p = p-1