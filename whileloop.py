# the general syntax of while loop is
# while test/codition
# code statement
# else:
# final code statement
'''
x=1
while x<10:
     print(x)
     x+=1
else:
     print('loop completed')
'''


#pass,continue and break
'''
y=1
while y<10:
    print('y is currently:',y)
    print('y is still less than 10 , adding 1 to y')
    y+=1

    if(y==5):
        print('y==5')
    else:
        print('continuing')
'''
# for break
y=1
while y<10:
    print('y is currently:',y)
    print('y is still less than 10 , adding 1 to y')
    y+=1

    if(y==5):
        print('y==5')
        break
    else:
        print('continuing')

