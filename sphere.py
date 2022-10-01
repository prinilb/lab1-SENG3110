import math

def surfaceArea(rad):
    surfaceArea = 4 * math.pi * pow(rad,2)
    return round(surfaceArea,2)

def volume(rad):
    volume = (4 / 3) * math.pi * pow(rad,3)
    return round(volume,2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Surface Area of a Sphere = ", surfaceArea(radius))
    print("\nThe Volume of a Sphere = ", volume(radius))
    

if __name__ == '__main__':
    prompt()


# surfaceArea 
# A=4πr^2
#

# volume 
# V=4/3πr^3
#
