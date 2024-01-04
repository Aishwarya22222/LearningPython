# loop/repeatation/iteration
# repeatation of statements upto specified condition

#  for loop
numbers=[1,2,3,4,5,3,5,6,7,8,89]
for num in numbers:
     print (num)

for x in numbers: # condition use gareko
     if x%2==0:
         print(x)

# total sum
total=0
for num in numbers:
    total+=num
    print(total)

for letter in 'programming':
     print(letter)

#range function 
for y in range(1,10):
    print(y)

for a in range(0,101,10): # 10 ko difference ma output niklincha
     print(a)

#nested loop(loop inside loop)
color=['yellow','orange','black','pink']
fruits=['kiwi','banana','mango','apple']
for looks in color:
     for name in fruits:
          print(looks,name)


