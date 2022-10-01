import cone
import cube
import cuboid
import cylinder
import equiTriangle
import sphere
import trapezoid
import triangle

def main():

    while True:
        print("\nWelcome to the Geometry Program\n")
        print("1. Sphere")
        print("2. Cylinder")
        print("3. Cone")
        print("4. Cuboid")
        print("5. Equilateral Triangle")
        print("6. Cube")
        print("7. Trapezoid")
        print("8. Triangle")
        print("0. Quit")

        selection = int(input("\nPlease enter your selection: "))
        if selection == 1:
            sphere.prompt()
        elif selection == 2:
            cylinder.prompt()
        elif selection == 3:
            cone.prompt()
        elif selection == 4:
            cuboid.prompt()
        elif selection == 5:
            equiTriangle.prompt()
        elif selection == 6:
            cube.prompt()
        elif selection == 7:
            trapezoid.prompt()
        elif selection == 8:
            triangle.prompt()
        if selection == 0:
            print("\nProgram Terminating...\n")
            break

if __name__ == '__main__':
    main()