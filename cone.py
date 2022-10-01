import math

def slant(rad, hi):
    sl = math.sqrt(pow(rad,2) + pow(hi,2))
    return round(sl,2)

def surfaceArea(rad, hi):
    s = math.pi * rad * (rad + math.sqrt(pow(hi,2) + pow(rad,2)))
    return round(s,2)

def volume(rad, hi): # V=πr^2 * h/3
    v = (math.pi * pow(rad,2)) * (hi / 3)
    return round(v,2)

def latSurf(rad, hi): # πr*sqrt(h^2+r^2)
    l = (math.pi * rad) * math.sqrt(pow(hi,2) + pow(rad,2))
    return round(l,2)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("CONE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the Radius of a Cone :"))
    height = int(input("Please Enter the Height of a Cone :"))

    print("\nLength of a Side (Slant) of a Cone = ", slant(radius, height))
    print("\nThe Surface Area of a Cylinder = ", surfaceArea(radius, height))
    print("\nThe Volume of a Cone = ", volume(radius, height))
    print("\nThe Lateral Surface Area of a Cone = ", latSurf(radius, height))


if __name__ == '__main__':
    prompt()

# slant 
# sqrt(r squared + h squared)
#

# surfaceArea 
# A=πr(r+*sqrt(h^2+r^2))
#

# volume 
# V=πr^2 * h/3


# latSurf 
# πr*sqrt(h^2+r^2)




