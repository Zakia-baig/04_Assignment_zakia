from colorama import Fore, Style, init
import time

# Initialize colorama
init()

def print_slow(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def mad_libs_game():
    # Welcome message
    print_slow(Fore.CYAN + "\n=== 📝 MAGICAL MAD LIBS GENERATOR 📝 ===" + Style.RESET_ALL)
    print_slow(Fore.YELLOW + "Let's create a funny story together!" + Style.RESET_ALL)
    
    # Get inputs with different colors
    adj1 = input(Fore.GREEN + "Enter an adjective: " + Style.RESET_ALL)
    noun1 = input(Fore.MAGENTA + "Enter a noun: " + Style.RESET_ALL)
    verb1 = input(Fore.BLUE + "Enter a verb (past tense): " + Style.RESET_ALL)
    adverb1 = input(Fore.RED + "Enter an adverb: " + Style.RESET_ALL)
    adj2 = input(Fore.GREEN + "Enter another adjective: " + Style.RESET_ALL)
    noun2 = input(Fore.MAGENTA + "Enter another noun: " + Style.RESET_ALL)
    
    # Story template
    story = f"""
{Fore.CYAN}🌟 Your Magical Story 🌟{Style.RESET_ALL}
    
Once upon a time, there was a {Fore.GREEN}{adj1}{Style.RESET_ALL} {Fore.MAGENTA}{noun1}{Style.RESET_ALL} 
who {Fore.BLUE}{verb1}{Style.RESET_ALL} {Fore.RED}{adverb1}{Style.RESET_ALL} through the forest. 
On the way, they found a {Fore.GREEN}{adj2}{Style.RESET_ALL} {Fore.MAGENTA}{noun2}{Style.RESET_ALL}!
"""
    
    # Print the story with a dramatic pause
    print("\nGenerating your story", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    print_slow(story)
    
    # Play again option
    print_slow(Fore.YELLOW + "\nWould you like to create another story? (yes/no)" + Style.RESET_ALL)
    return input().lower().strip() == 'yes'

def main():
    while True:
        if not mad_libs_game():
            print_slow(Fore.CYAN + "\nThanks for playing! Come back soon! 👋" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
