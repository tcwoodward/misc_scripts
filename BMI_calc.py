# Start of Program

print("\nBMI Calculator")

# Choosing method of BMI calculation

x = input("Metric or Imperial (M or I):")

# Calculating BMI by Imperial Standards
    
if (x == "I" or x == "i"):
    feet = int(input("\nPlease Enter Height: \nFeet: "))
    inches = int(input("Inches: "))

    foot = 12
    height_in = foot * feet + inches

    weight_lbs = int(input("\nPlease Enter Weight (lbs): "))

    bmi = weight_lbs / (height_in ** 2) * 703
    
# Calculating BMI by Metric Standards
    
elif (x == "M" or x == "m"):
    kg = float(input("\nPlease Enter Weight (kg): "))
    cm = float(input("\nPlease Enter Height (cm): "))
    
    m = cm / 100
    bmi = kg / (m * m)
    
# Default fallback
    
else:
    input("Please restart the program and try again. Press any key to exit.")	

# Printout of results

print("\nYour BMI is:", round(bmi, 2))
if (bmi <= 18.5):
    print("You are underweight.")
elif (bmi > 25 and bmi < 30):
    print("You are overweight.")
elif (25 > bmi and bmi > 18.5):
    print("You are at a healthy weight.")
else:
    print("You are obese.")

input("Press any key to exit.")

# End of program
