def surfaceArea(side):
    s = 6 * pow(side,2)
    return round(s,2)

def volume(side):
    v = pow(side,3)
    return round(v,2)

def latSurf(side):
    l = 4 * pow(side,2)
    return round(l,2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("CUBE")
    print("------------------------------------------------------------")

    side = int(input("Please Enter the Length of any Side of a Cube :"))

    print("\nThe Surface Area of a Cube = ", surfaceArea(side));
    print("\nVolume of a Cube = ", volume(side))
    print("\nLateral Surface Area of a Cube = ", volume(side))


if __name__ == '__main__':
    prompt()


# surfaceArea 
# 6 * side squared
#


# volume 
# side cubed
#

# latSurf 
# 4 * side squared 
#