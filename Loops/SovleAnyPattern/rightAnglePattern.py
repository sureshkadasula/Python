"""
Right angled Triangle : https://www.youtube.com/watch?v=fX64q6sYom0&t=63s
"""
rows = int(input("Enter row count : "))
for i in range(rows):
    for j in range(i ,rows):
        print("*" , end=" ")
    print()