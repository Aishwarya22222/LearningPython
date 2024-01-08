# **kwargs-> it builds a dictionary of key value pair

def myFunction(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favorite fruit is {kwargs['fruit']}")
    else:print('not a favorite fruit')


myFunction(fruit='orange')