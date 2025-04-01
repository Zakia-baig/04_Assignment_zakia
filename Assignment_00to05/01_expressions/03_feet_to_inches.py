# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.


# Feet to Inches Converter
INCHES_PER_FOOT = 12  # Conversion constant

print("Feet to Inches Converter")
print("(1 foot = 12 inches)")
print("-----------------------")

while True:
    try:
        # Get input from user
        feet = float(input("Enter measurement in feet (or 'q' to quit): "))
        
        # Calculate inches
        inches = feet * INCHES_PER_FOOT
        
        # Determine singular/plural wording
        foot_word = "foot" if feet == 1 else "feet"
        inch_word = "inch" if inches == 1 else "inches"
        
        # Display result
        print(f"\n{feet} {foot_word} = {inches} {inch_word}\n")
        
    except ValueError:
        # Exit on non-numeric input
        print("\nThank you for using the converter!")
        break