given_num = int(input("Enter a num: "))
sum = 0
for i in range(1 , given_num):
    if given_num % i == 0:
        sum = sum + i
if sum == given_num:
    number_is = "Perfect Number"
else:
    number_is = "Not a Perfect Number"
print(number_is)