# polymorphism -> method overriding function ko name same cha tara kaam different)

class Bird():
    def intro(self):
        print('there are many types of bird')
    def fly(self):
        print('some birds can fly but some cannot')

class Parrot(Bird):
    def fly(self):
        print('parrot can fly')

class Kiwi(Bird):
    def fly(self):
        print('kiwi cannot fly')
    
obj_bird=Bird()
obj_bird.intro()
obj_bird.fly()

obj_parrot=Parrot()
obj_parrot.fly()

obj_kiwi=Kiwi()
obj_kiwi.fly()
obj_kiwi.intro()
