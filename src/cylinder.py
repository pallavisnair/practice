
class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        pass

    def volume(self):
        pi = 3.14
        Vol = pi*(self.radius**2)*self.height
        return Vol
        pass

    def surface_area(self):
        pi=3.14
        Area = (2*pi*self.radius*self.height)+(2*pi*(self.radius**2))
        return Area

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())
