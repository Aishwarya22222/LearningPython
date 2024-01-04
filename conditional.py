# conditional statement is used to check whether the condition is met or not
# if else
# elif

x=int(input('Enter the value of x: '))
if x%2==0:
    print(x, 'is a even number')
else:
    print(x, 'is a odd number')



year=int(input('Enter the year to check if leap year or not: '))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year, 'is a leap year')
else:
    print(year,'is not a leap year')


# write a program to check if a particular number is ultiple of 5 or not

if 15%5==0:
    print('multiple of 5')
else:
    print('not a multiple of 5')


# elif is used to check the multiple condition

a=int(input('Enter the number: '))
if a<0:
    print(a, 'is a negative number')
elif a>0:
    print(a,'is a positive number')
else:
    print('zero')


x=10
y=15
z=12
if x>y and x>z:
    print('x is greater')
elif y>z and y>x:
    print('y is greater')
else:
    print('z is greater')