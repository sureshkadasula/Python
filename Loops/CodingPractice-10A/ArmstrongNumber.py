num = input("Enter number: ")
Kth_poer = len(num)
sum = 0
for each_char in num:
    sum = sum + int(each_char) ** Kth_poer
if sum == int(num):
    number_is = "Armstrong Number"
else:
    number_is = "Not an Armstrong Number"
print(number_is)