# characteristics of an object is called attribute.
# suntax for creating object is
# self.attributename=value
# eg. self.email='ram@gmail.com'
# there is a special method called __init__() which is called automatically when a object
# is created from the class


class Student:
    level='bachelor'

    def __init__(self,name):
        self.stdname=name
        self.roll_no=25
a= Student(name='Aishwarya')
print(a.stdname)
print(a.roll_no)
print(a.level)