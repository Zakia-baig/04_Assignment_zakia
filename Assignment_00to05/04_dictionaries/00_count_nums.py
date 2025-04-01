"""This program counts the number of times each number appears in a list. 
It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 
Enter a number: 12 Enter a number: 3 appears 3 times.
4 appears 2 times. 6 appears 1 times. 12 appears 1 times."""



def count_numbers():
    number_counts = {}
    
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        
        try:
            number = int(user_input)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")
            continue
        
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1
    
    print("\nNumber counts:")
    for number, count in sorted(number_counts.items()):
        print(f"{number} appears {count} {'time' if count == 1 else 'times'}.")

# Run the program
count_numbers()