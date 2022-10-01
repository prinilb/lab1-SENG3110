import math

def area(base1, base2, height):
    area = ((base1 + base2) * height) / 2
    return round(area,2)

def median(base1, base2, height):
    median = (base1 + base2) / 2
    return round(median,2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("TRAPEZOID")
    print("------------------------------------------------------------")

    base1 = int(input("Please Enter the base1 :"))
    base2 = int(input("Please Enter the base2 :"))
    height = int(input("Please Enter the height :"))

    print("\nArea of a Trapezoid = ", area(base1, base2, height))
    print("\nMedian of a Trapezoid = ", median(base1, base2, height))

if __name__ == '__main__':
    prompt()


# area 
# A = � (a + b) h
#

# median
# average of the length of the bases
#



