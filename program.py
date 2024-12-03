from rectangle import rect_area
from rectangle import pre
from circle import circ_area
from circle import circ_perimeter
from d_graphics.cuboid import cuboid_surface
from d_graphics.cuboid import cuboid_volume
from d_graphics.sphere import sphere_surface
from d_graphics.sphere import sphere_volume


length =int(input("enter the length:"))
breadth = int(input("enter the bredth:"))
print("Rectangle Area: ",rect_area(length, breadth))
print(f"Rectangle Perimeter: {pre(length,breadth)}")


radius = int(input("enter the radius:"))
print(f"Circle Area: {circ_area(radius)}")
print(f"Circle Perimeter: {circ_perimeter(radius)}")


heightt = int(input("enter the height:"))
lengthh = int(input("enter the lengt:"))
breadthh = int(input("enter the bredth:"))
print(f"Cuboid Surface Area: {cuboid_surface(lengthh, breadthh, heightt)}")
print(f"Cuboid Volume: {cuboid_volume(lengthh, breadthh, heightt)}")

radiuss = int(input("enter the radius:"))
print(f"Sphere Surface Area: {sphere_surface(radiuss)}")
print(f"Sphere Volume: {sphere_volume(radiuss)}")
