number_of_inputs = int(input("Enter no of inputs: "))
first_input = int(input(f"Enter first input: "))
greatest_number = first_input

for i in range(number_of_inputs - 1):
    number = int(input(f"Enter input{i}: "))
    if number > greatest_number:
        greatest_number = number

print(greatest_number)
