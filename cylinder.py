# inspiration code for Python Unit Testing Project
import math

def surfaceArea(rad, hi):
    surfaceArea= (2 * math.pi * rad * hi) + (2 * math.pi * pow(rad,2))
    return round(surfaceArea,2)

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return round(volume,2)

def prompt():
    print()
    print("----------------------------------------------------------")
    print("CYLINDER")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    height = int(input("Please Enter the height :"))

    print("\nThe Volume of a Cylinder = ", volume(radius, height))
    print("\nThe Surface Area of a Cylinder = ", surfaceArea(radius, height))

if __name__ == '__main__':
    prompt()


# surfaceArea 
# 2 times pi times rad to the 2nd power times height
#