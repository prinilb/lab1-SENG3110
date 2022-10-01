import math

def perimeter(sideOne, sideTwo, sideThree):
    perimeter = sideOne + sideTwo + sideThree
    return round(perimeter, 2)

def semi_perimeter(sideOne, sideTwo, sideThree):
    semi_perimeter = (perimeter(sideOne, sideTwo, sideThree)) / 2
    return round(semi_perimeter, 2)

def area(sideOne, sideTwo, sideThree):
    s = semi_perimeter(sideOne, sideTwo, sideThree)
    area = math.sqrt(s * (s - sideOne) * (s - sideTwo) * (s - sideThree))
    return round(area, 2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("TRIANGLE")
    print("------------------------------------------------------------")

    sideOne = int(input("Please Enter the First side of a Triangle :"))
    sideTwo = int(input("Please Enter the Second side of a Triangle :"))
    sideThree = int(input("Please Enter the Third side of a Triangle :"))

    print("\nThe Perimeter of a Triangle = ", perimeter(sideOne, sideTwo, sideThree))
    print("\nThe Semi Perimeter of a Triangle = ", semi_perimeter(sideOne, sideTwo, sideThree))
    print("\nThe Area of a Triangle = ", area(sideOne, sideTwo, sideThree))
   


if __name__ == '__main__':
    prompt()


# perimeter
# add all three sides together 
#

# semi_perimeter
# perimeter divided by two
#


# area
# Area = √[s(s-a)(s-b)(s-c)]
#




