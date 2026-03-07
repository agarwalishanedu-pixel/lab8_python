"""
Program Name: Lab 8 (Main File)
My name: Ishan Agarwal
Purpose: This program is meant to deepen my understanding of functions in python. Also this is used to make multiple different calculations for circles and rectangles.
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
    # Calculate area of circle
    if option == "1":
        radius: float = float(input("Enter the radius of the circle: "))
        print("")
        final_value: float = c.area(radius)
        print(f"The area of the circle is {final_value}.")
        print("")
    
    # Calculate circumference of circle
    elif option == "2":
        radius: float = float(input("Enter the radius of the circle: "))
        print("")
        final_value: float = c.circumference(radius)
        print(f"The circumference of the circle is {final_value}.")
        print("")
        
    # Calculate area of rectangle 
    elif option == "3":
        width: float = float(input("Enter the width of the rectangle: "))
        height: float = float(input("Enter the height of the rectangle: "))
        print("")
        final_value: float = r.area(width, height)
        print(f"The area of the rectangle is {final_value}.")
        print("")

    # Calculate perimeter of rectangle 
    elif option == "4":
        width: float = float(input("Enter the width of the rectangle: "))
        height: float = float(input("Enter the height of the rectangle: "))
        print("")
        final_value: float = r.perimeter(width, height)
        print(f"The perimeter of the rectangle is {final_value}.")
        print("")

    # Exit loop
    elif option == "5":
        print("Goodbye!")
        run = False

    # Continuation message
    if run:
        input("Press Enter to continue...")
        print("")