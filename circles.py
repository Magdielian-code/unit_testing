from math import pi
def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Radius must be an integer or float.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    
    return pi*(r**2)

 