# The program asks the user for input N (positive integer) and reads it
input_n = input("Please type in a positive integer N\n")

# Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
numbers = {}
for i in range(int(input_n)):
    input_numbers = input(f"Please type in the No.{i+1} numbers\n")
    numbers[i] = input_numbers

# In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
input_x = input("Please type in an integer X\n")
if input_x in numbers.values():
    print(f"The index of this integer X is {1 + list(numbers.values()).index(input_x)}")
else:
    print("-1")


