"""In this program we show an example of using dictionaries to keep track of information in a phonebook."""


def read_phone_numbers():
    """Create a phonebook by collecting names and numbers from the user."""
    phonebook = {}
    print("➤ Phonebook Entry Mode (Leave name blank to finish)")
    
    while True:
        name = input("\n✎ Name: ").strip()
        if not name:
            break
        number = input("☎ Number: ").strip()
        phonebook[name] = number
        print(f"✓ Added: {name}")
    
    return phonebook


def print_phonebook(phonebook):
    """Displays all contacts in the phonebook."""
    if not phonebook:
        print("\nℹ Phonebook is empty")
        return
    
    print("\n══════ Your Contacts ══════")
    for name, number in phonebook.items():
        print(f"• {name:15} → {number}")
    print("═══════════════════════")


def lookup_numbers(phonebook):
    """Allows number lookup by name."""
    if not phonebook:
        print("No contacts to lookup")
        return
    
    print("\n➤ Lookup Mode (Leave blank to exit)")
    while True:
        name = input("\n⌕ Name: ").strip()
        if not name:
            break
        if name in phonebook:
            print(f"✓ Found: {phonebook[name]}")
        else:
            print(f"✗ Not found")


def main():
    print("\n★★★★★ PYPHONEBOOK ★★★★★")
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    print("\nThank you!")


if __name__ == '__main__':
    main()