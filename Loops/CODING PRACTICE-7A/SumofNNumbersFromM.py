M = int(input("Enter M Value: "))
N = int(input("Enter N Value : "))
count = M
sum = 0
while count < M + N:
    sum = sum + count
    count = count + 1
print(sum)
