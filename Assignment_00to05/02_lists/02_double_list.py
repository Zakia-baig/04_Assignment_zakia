"""Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]"""



numbers: list[int] = [1, 2, 3, 4]  # Original list

for i in range(len(numbers)):  # Loop through each index
        numbers[i] *= 2        # Shortcut to double the element
print(numbers)                 # Prints [2, 4, 6, 8]


