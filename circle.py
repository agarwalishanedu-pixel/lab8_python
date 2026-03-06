"""
Program Name: Lab 8 (Circle.py)
My name: Ishan Agarwal
Purpose: This program is meant to deepen my understanding of functions in python
Starter Code: None
Date: 03/06/2026

Functions: 
 area(radius): This function is used to calculate and return the area of a circle.
 circumference(radius): This function is used to calculate and return the area of a circle. 
"""

import math

def area(radius):
    """
    This calculates the area of a circle:
    - It takes in the 'radius' (float) as a parameter
    - It returns a float value of the area
    """
    
    return math.pi * (radius ** 2)

def circumference(radius):
    """
    This calculates the circumference of a circle:
    - It takes in the 'radius' (float) as a parameter
    - It returns a float value of the circumference
    """

    return 2 * math.pi * radius