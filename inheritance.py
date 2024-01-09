# inheritance is to form a new classes from the classes that have been already defined.
# The newly formed class is called derive class and the class that we derive from are called base class.
# The derived class override or extend the functionality of base class.

class Animal():
    def __init__(self):
        print('Animal class created')

    def Whois(self):
        print('Animallllssssss')
    
    def eat(self):
        print('Animal who eat')

# derive class create gareko(inheritance)
class Dog(Animal):
    def Whois(self):
        print('Dog')

    def speak(self):
        print('Bhau Bhau')

a=Animal()
print(a)
a.Whois()
a.eat()

b=Dog()
b.Whois()
b.eat()
b.speak()

