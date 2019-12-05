

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
        return 'Rectangle 2nd: \nwidth= {0}\nheight= {1}'.format(self.width, self.height)
    
    # Will print this upon creation of object
    def __str__(self):
        return 'Auto Rectangle Print 1st:\nwidth= {0}\nheight= {1}'.format(self.width, self.height)
    
    #representation, string that shows how to build object again (anytime called not just in print)
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    # This helps compare objects to other objects, take out this function and figure 5 is false
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
            # or return (self.width, self.height) == (other.width, other.height)
        else:
            return False
    
# %% Program
        
# Makes object from class
r1 = Rectangle(5,10)

# Now prints because of the __str__
print(r1)

# prints perim value as expected
print(r1.perimeter())
#print(r1.to_string())

# Makes second object from class
r2 = Rectangle(5,10)

# Not the same object
print(r1 is not r2)

#Figure 5, false unless __eq__ method is used
print(r1 == r2)

