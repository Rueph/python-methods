

# Write functions that do the following:
# 1. Returns area and perimeter of a circle.
import math

def area_circle(diameter):
    radius = diameter//2
    area = 3.14*radius**2 
    perimeter = 2*math.pi*radius
    return area, perimeter

diameter = 8
area, perimeter = area_circle(diameter)
print(f"The area of a circle witth diameter{diameter} has an area of {area}")
print(f"The perimeter of a circle with diameter {diameter} is {perimeter}")

# 2. Returns volume of a sphere.

def volume_sphere(diameter):
    radius = diameter//2
    sphere_volume = 4/3*math.pi*radius**3
    return sphere_volume

diameter = 90
result= volume_sphere(diameter)
print(f"The volume of the sphere with diameter of {diameter}cm is {result}cm")


# 3. Write a function to check whether a number is prime or not


def prime_number(num):
    if num < 2:
        return "The number is not a prime number"
    
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return "The number is not a prime number"
        divisor += 1

    return "The number is a prime Number"
    
num = 48
result = prime_number(num)
print(result)


# 4. Write a function to check whether a number is odd or even


def is_even_or_odd(num):
    #Check if the number is even
    
    if num % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"
    
num = 7
result = is_even_or_odd(num)
print(result)