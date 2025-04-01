"""There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

Here is an example run of the program (user input is in bold italics):

How many (apple) do you want?: 2

How many (durian) do you want?: 0

How many (jackfruit) do you want?: 1

How many (kiwi) do you want?: 0

How many (rambutan) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5

"""

def main():
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }
    
    print("Welcome to the Fruit Shop!")
    print("Available fruits and their prices:")
    
    # Display available fruits with prices
    for fruit, price in fruits.items():
        print(f"- {fruit.capitalize()}: ${price:.2f} each")
    
    total_cost = 0
    
    # Get quantity for each fruit
    for fruit_name, price in fruits.items():
        while True:
            try:
                amount = int(input(f"How many {fruit_name}s would you like to buy? (0 to skip): "))
                if amount >= 0:
                    total_cost += price * amount
                    break
                else:
                    print("Please enter a positive number or 0.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    
    # Display total with formatting
    print(f"\nYour total is: ${total_cost:.2f}")


if __name__ == '__main__':
    main()
