""""
Left Angle triangle
"""
rows = int(input())
for i in range(rows):
    for j in range(i+1):
        print("*" , end=" ")
    print()