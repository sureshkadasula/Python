N = int(input("Enter number: "))
for value in range(1 , N + 1):
    if value == N:
        print("+ " * value)
    else:
        print("*" * value)
        # if value == N:
        #     print("+ "* value)