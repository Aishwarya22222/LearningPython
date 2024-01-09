# methods are the function defined inside the body of the clss. They are used to perform the operation 
# with the attribute of the objects. Methods are the key concept of OOP paradigm and essential for 
# large application

class Circle:
    pi=3.14

    def __init__(self,radius=1):
        self.r=radius
        self.area=self.pi*radius*radius
    
    def setRadius(self,r):
        self.radius=r
        self.area=self.pi*r*r

    def getCircumference(self):
        self.result=2*self.pi*self.radius

a=Circle()
print(a.r)
print(a.area)

a.setRadius(4)
print('new radius is:',a.radius)
print('new area is:',a.area)

a.getCircumference()
print(a.result)

b=Circle()
b.setRadius(5)
print(b.area)
