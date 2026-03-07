"""
Program Name: Lab 8 (Main File)
My name: Ishan Agarwal
Purpose: This program is meant to deepen my understanding of functions in python. Also this is used to calcu
Starter Code: None
Date: 03/06/2026 
"""

# Importing the files with aliases
# Using aliases are important especially because both of the files have a function called Area. 
import circle as c
import rectangle as r

run: bool = True

while run:
    print("Geometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")
    print("")
    
    #user inputs their choice
    option: str = input("Enter your choice (1-5): ")
    print("")

    # Evaluate their choice
    if option == "1":
        radius = float(input("Enter the radius of the circle: "))
        print("")
        final_value = c.area(radius)
        print(f"The area of the circle is {final_value}.")
        print("")
    
    elif option == "2":
        radius = float(input("Enter the radius of the circle: "))
        print("")
        final_value = c.circumference(radius)
        print(f"The circumference of the circle is {final_value}.")
        print("")


