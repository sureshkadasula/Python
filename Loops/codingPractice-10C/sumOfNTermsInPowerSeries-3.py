X = int(input())
N = int(input())
sum = 0
power = 2
diff = 0
for num in range(N,0,-2):
    sum = sum + X ** power
    power = power + 2
    diff = diff - (X**power)
    power = power + 2
print(sum)