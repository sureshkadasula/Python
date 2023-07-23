X = int(input("Enter value of X : "))
N = int(input("Enter value of N : "))
sum = 0
for i in range(1 , 2*(N) ,+2):
    sum = sum + X ** i
print(sum) 