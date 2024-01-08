# **kwargs-> it builds a dictionaryof key value pair

def myFunction(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favorite fruits is {kwargs['fruit']}")
    else:print('not a favorite fruit')


myFunction(fruit='orange')