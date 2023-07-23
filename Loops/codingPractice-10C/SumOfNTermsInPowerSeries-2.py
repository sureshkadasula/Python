X = int(input("Enter value of x : "))
N = int(input("Enter value of Y : "))
sum = 0
power =2
for i in range(1 , N + 1):
    sum = sum + X ** power
    power = power + 2
print(sum)