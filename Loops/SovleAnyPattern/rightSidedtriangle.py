""""
Right Sided traingle pattern
"""
rows = int(input("Enter row count : "))
for i in range(rows):
    for j in range(i , rows):
        print('.' , end=" ")
    for k in range(i+1):
        print("*" , end=" ")
    print()