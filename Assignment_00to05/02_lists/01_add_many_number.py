# Write a function that takes a list of numbers and returns the sum of those numbers.

"""
    Takes in a list of numbers and returns the sum of those numbers.
    """

def calculate_sum(numbers: list[int]) -> int:
    """
    Takes a list of integers and returns their total sum.
    
    Args:
        numbers: A list of integers to be summed.
    
    Returns:
        The sum of all numbers in the list.
    """
    return sum(numbers)

def main() -> None:
    # Define a list of numbers
    sample_numbers: list[int] = [10, 20, 30, 40, 50]
    
    # Compute the sum
    result: int = calculate_sum(sample_numbers)
    
    # Print the result
    print(f"The sum of the numbers is: {result}")

if __name__ == "__main__":
    main()