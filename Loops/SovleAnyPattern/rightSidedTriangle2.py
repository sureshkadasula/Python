"""
Right Sided triangle 
1.Increasing Space
2.Decreasing Space
"""
rows = int(input())
for i in range(rows):
    for j in range(i+1):
        print("." , end=" ")
    for k in range(i , rows):
        print("*" , end=" ")
    print()