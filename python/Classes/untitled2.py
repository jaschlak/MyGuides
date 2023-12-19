

# %% Library

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area (self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width * self.height)
    
    def to_string(self):
        return 'Rectangle: width = {0}, height = {1}'.format(self.width, self.height)
    
# %% Program
        
r1 = Rectangle(5,10)

print(str(r1))
print(r1.to_string())