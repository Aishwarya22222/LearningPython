# a lambda expression is used to create anonymous function, this basically means we can quickly 
# make ad-hoc function without neeeding to write def keyword.

# def square(x):
#     return x**2

square= lambda x: x**2

result=square(4)
print(result)


# filter wala ma lambda use garera
mylist=[1,2,3,4,5,6,7,8,9,]
result=list(filter(lambda num: num%2==0,mylist))
print(result)


numbers=[1,2,3,4,5,6,7,8,9,]
a=list(map(lambda num: num**2,numbers))
print(a)