def surfaceArea(length, width, height):
    sa = (2 * (length * width)) + (2 * (length * height)) + (2 * (height * width))
    return round(sa,2)

def volume(length, width, height):
    v = length * width * height 
    return round(v,2)

def latSurf(length, width, height):
    l = (2 * height) * (length + width)
    return round(l,2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("CUBOID")
    print("------------------------------------------------------------")

    length = int(input("Please Enter the Length :"))
    width = int(input("Please Enter the Width :"))
    height = int(input("Please Enter the Height :"))

    print("\nThe Surface Area of a Cuboid = ", surfaceArea(length, width, height));
    print("\nVolume of a Cuboid = ", volume(length, width, height))
    print("\nLateral Surface Area of a Cuboid = ", latSurf(length, width, height))


if __name__ == '__main__':
    prompt()


# surfaceArea 
# SA=2lw+2lh+2hw


# volume 
# Length � Width � Height
    

# latSurf 
# 2 * h * (l + w)
#


