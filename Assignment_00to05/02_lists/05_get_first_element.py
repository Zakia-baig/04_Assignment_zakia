"""Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the 
first element in the list. The list is guaranteed to be non-empty.
 We've written some code for you which prompts the user to input the list one element at a time."""


def get_first_element(lst: list) -> None:
    """Prints the first element of the given list.
    
    Args:
        lst: A non-empty list whose first element will be printed.
    """
    print(lst[0])


def get_list_from_user() -> list:
    """Prompts the user to enter list elements one by one.
    
    Returns:
        A list containing all the elements entered by the user.
    """
    lst = []
    print("Enter the elements of the list one by one.")
    print("Press Enter (empty input) to finish.")
    
    while True:
        elem = input("Enter an element: ").strip()
        if not elem:  # Stop if the user enters nothing
            break
        lst.append(elem)
    
    return lst


def main() -> None:
    """Main function to execute the program."""
    user_list = get_list_from_user()
    if user_list:  # Ensure the list is not empty
        get_first_element(user_list)
    else:
        print("The list is empty. No first element to display.")


if __name__ == '__main__':
    main()