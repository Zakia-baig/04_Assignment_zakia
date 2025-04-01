# Write a program that continually reads in mass from the user and then outputs the equivalent energy using
# Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass 
# and energy are interchangeable and are related by the above equation.
# You should ask the user for mass (m) in kilograms and use a constant value for 
# the speed of light -- C = 299792458 m/s.

# Einstein's mass-energy equivalence calculator
C = 299792458  # Speed of light in m/s

print("Einstein's Mass-Energy Equivalence Calculator")
print("E = m * C^2")
print()

while True:
    try:
        # Get mass input from user
        mass = float(input("Enter kilos of mass (or 'q' to quit): "))
        
        # Calculate energy
        energy = mass * (C ** 2)
        
        # Display calculation details
        print("\n e = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")
        
    except ValueError:
        # Handle non-numeric input (including 'q' to quit)
        print("\nThanks for using the calculator!")
        break