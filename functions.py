# function -> a block of code to perform the particular task
# function is reusable
# call the function using parethesis() eg. demo()
# define th function using def eg. def demo():...

# define the function
def demoFunction():
    print('this is a function')
# call the function
demoFunction()

# function with arguments
#define the function
def addFunction(x,y):
    sum=x+y
    print('the sum is',sum)

# call the function with arguments
addFunction(20,30)


# function with return type
#define the function
def testFunction(num1,num2):
    data=num1+num2
    return data
# call the function
result=testFunction(5,10)
print('the result is',result)
test=testFunction(7,8)
print(test)



#define the function
def checkEven(x):
    if x%2==0:
        return'even number'
    else:
        return'odd number'
#call the function
check=checkEven(10)
print(check)
