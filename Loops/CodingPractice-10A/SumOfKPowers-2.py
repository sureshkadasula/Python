N = input("Enter a number: ")
Kth_power = len(N)
sum = 0
for each_char in N:
    sum = sum + int(each_char) ** Kth_power
print(sum)