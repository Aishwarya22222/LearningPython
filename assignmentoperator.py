# assignment operation is used to assign the value to a variable
# = -> value assign 
# += -> x+=y is same as x=x+y
# -= -> x-=y is same as x=x-y
# *= -> x=y is same as x=x*y
# /= -> x/=y is same as x=x/y
# %= -> x%=y is same as x=x%y
# **= -> x**=y is same as x=x**y
# //= -> x//=y is same as x=x//y

x=20
y=30
x+=y
print('value of x is',x)

x-=10
print('value of x',x)

x=60
y=10
x/=y
print('value of x',x)

x//=75
print('value of x',x)

 #comparison operator
# it is used to compare the values
# == -> equal to
# != ->not equal to
# <,>,<=,.>=

a=5
b=5
print(a==b)
print(a!=b)

# logical operator
# or -> returns true if any one condition is true otherwise false
# and -> returns true if all the condition are true otherwise false
# not -> reverse the final result

print (89<10 and 45>7)
print (5>2 or 3<6)
print (not(5>2 or 3<6))


# membership operator

# it is used to check if a sequence is present in an object or not
# in -> returns true if a specified sequence with a specified value present in an object
# not in-> returns true if a specified sequence with a specified value is not present in an object

list1=['mango','banana','orange','apple']
print('orange' in list1)
print('cherry' in list1)

print('guava' not in list1)