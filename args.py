# *args-> when a function parameter starts with astrik, it allows for an arbitary number of argument and
#         function takes them in a tuple of value
def myFunction(*args):
    return sum(args)
    
x=myFunction(10,20,30,40,50,60)
print(x)