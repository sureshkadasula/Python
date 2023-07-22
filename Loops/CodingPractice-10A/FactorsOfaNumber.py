num = int(input())
fact_with_space = ""
for each_num in range(1 , num + 1):
    if (num % each_num) == 0:
        fact_with_space = fact_with_space + str(each_num) + " "
print(fact_with_space)