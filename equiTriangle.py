import math

def area(side):
    area = (math.sqrt(3) * pow(side,2)) / 4
    return round(area,2)

def perimeter(side):
    perimeter = side * 3
    return round(perimeter,2)

def semi_perimeter(side):
    semi_per = perimeter(side) / 2
    return round(semi_per,2)

def altitude(side):
    a = (side * math.sqrt(3)) / 2
    return round(a,2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("EQUILATERAL TRIANGLE")
    print("------------------------------------------------------------")

    side = int(input("Please Length of any side of an Equilateral Triangle :"))

    print("\nArea of an Equilateral Triangle = ", area(side))
    print("\nPerimeter of an Equilateral Triangle = ", perimeter(side))
    print("\nSemi Perimeter of an Equilateral Triangle = ", semi_perimeter(side))
    print("\nAltitude of an Equilateral Triangle = ", altitude(side))
    
   


if __name__ == '__main__':
    prompt()

# area
# A  = √3 * a^2 / 4
#

# perimeter
# side times 3
#

# semi_perimeter
# perimeter divided by two
#


# altitude
# side * sqrt(3) / 2



