num = int(input())
sum = 0
for each_num in range(1 , num + 1):
    if num % each_num == 0:
        sum = sum + each_num
print(sum)