import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        timer_display = f'{minutes:02d}:{remaining_seconds:02d}'
        print(timer_display, end='\r')        # end='\r' to update the same line instead of creating new lines
        time.sleep(1)           # time.sleep(1) to create one-second intervals
        seconds -= 1
    
    print("Time's up!")

# Get user input
try:
    duration = int(input("Enter time in seconds: "))
    countdown_timer(duration)
except ValueError:
    print("Please enter a valid number of seconds.")
