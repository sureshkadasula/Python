"""
We have to give no of rows and cols as input:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
rows = int(input("Enter row count : "))
cols = int(input("Enter cols count : "))
for i in range(rows):
    for j in range(cols):
        print("*" ,end=" ")
    print()
    

