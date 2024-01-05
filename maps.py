# the map function allows you to map a function to an iterable object. This means you can call the same
#function to every itemof an iteraable such list

def square(num):
    return num**2

mylist=[1,3,5,6,7]
a=list(map(square,mylist))
print(a)


def check(name):
    if len(name)%2==0:
        return name
    else:
        return 'odd'

names=['madhav','roshan','manish','ram','hari']
result=list(map(check,names))
print(result)
