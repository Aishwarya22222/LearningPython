# similar to map but it print only filtered output

def checkeven(num):
    return num%2==0

numbers=[1,2,3,4,5,6,7,8,9,6,240,44,24,5,7]
result=list(filter(checkeven,numbers))
print(result)

# list of even numbers and odd numbers
numbers=[1,2,3,4,5,6,7,8,9,6,240,44,24,5,7]
even_no=[]
odd_no=[]

for num in numbers:
    if num%3==0:
        even_no.append(num)
    else:
        odd_no.append(num)

print('even numbers',even_no)
print('odd numbers',odd_no)