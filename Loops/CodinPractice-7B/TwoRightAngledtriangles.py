N=int(input("Enter a Number: "))
count = 1
while count <= 2:
    count_as_row = 1
    while count_as_row <= N:
        print(str(count_as_row) * count_as_row)
        count_as_row = count_as_row + 1
    count = count + 1