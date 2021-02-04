#!/bin/python3
""" 
This is a C/F calculator I made to help myself learn some of the basics of Python as is the first program/script
I've created from scratch! It is meant to be ran in a terminal as an executed program.
"""
# Start of program
print("This is a calculator for converting Fahrenheit and Celsius between each other.")

# Variables
F, C = "Fahrenheit", "Celsius"
prompt = "\nPlease enter your number for %s: "
results = "\n%d %s is %d %s."

# Begin program
x = input("\nPlease choose Fahrenheit or Celsius (F or C): ")

# Conditional Statements and Maths
if (x == "F" or x == "f"):
    f = float(input(prompt%F))
    c = (f - 32) / 1.8
    print(results%(f,F,c,C))
elif (x == "C" or x == "c"):
    c = float(input(prompt%C))
    f = c * 1.8 + 32
    print(results%(c,C,f,F))
else:
    print("\nPlease restart the calculator and try again.")  
    
input("\nPress any key to quit.")    
# End of program  
