class Rectangle:
    def __init__(self, length, breadth):
       
        self.length = length
        self.breadth = breadth

    def area(self):
        
        return self.length * self.breadth

    def perimeter(self):
       
        return 2 * (self.length + self.breadth)

    def compare_area(self, other):
        
        if not isinstance(other, Rectangle):
            raise ValueError("The other object is not a Rectangle")
        
        area_self = self.area()
        area_other = other.area()

        if area_self > area_other:
            return "This rectangle is larger."
        elif area_self < area_other:
            return "The other rectangle is larger."
        else:
            return "Both rectangles have the same area."


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)

print(f"Rectangle 1 Area: {rect1.area()}")          
print(f"Rectangle 2 Area: {rect2.area()}")          
print(f"Rectangle 1 Perimeter: {rect1.perimeter()}") 
print(f"Rectangle 2 Perimeter: {rect2.perimeter()}") 

print(rect1.compare_area(rect2))
