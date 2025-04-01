"""Fill out the function shorten(lst) which removes elements from the end of lst, 
which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main()
function for you which gets a list and passes it into your function once you run the program.
For the autograder to pass you will need MAX_LENGTH to be 3,
but feel free to change it around to test your program."""

MAX_LENGTH = 3  # Constant defining the maximum allowed length

def shorten(lst):
    """Removes elements from the end of the list until it is of length MAX_LENGTH.
    Prints each removed element.
    
    Args:
        lst: The list to be shortened (modified in-place).
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove and return the last element
        print(removed_item)


# Provided main() function (for testing)
def main():
    lst = ['a', 'b', 'c', 'd', 'e']
    shorten(lst)
    print("Final list:", lst)  # Should be ['a', 'b', 'c']

if __name__ == '__main__':
    main()