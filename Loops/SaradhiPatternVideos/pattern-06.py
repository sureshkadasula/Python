'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
rows = int(input("Enter row count : "))
for i in range(1 , rows+1):
    for j in range(i , rows):
        print(" " , end=" ")
    for j in range(i):
        print("*", end=" ")
    print()