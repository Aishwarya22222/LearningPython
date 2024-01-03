# list are similar to array in other programming, list contains more than one value
# list is mutable i.e elements inside list can be changed(add or remove)

fruits=['mango', 'banana', 'papaya','apple']
print(fruits)

#count the numbers of elements in a list use len()
print(len(fruits))

#indexing
print(fruits[0])
print(fruits[0][0])
print(fruits[0][2].upper())
print(fruits[1:4])

# .append()-> to add new element in the list at the last position
fruits.append('kiwi')
print(fruits)

# .pop()-> to remove element fro the list and by default it remove element of last position
fruits.pop()
print(fruits)

# to remove from speecific position use indexing taht is .pop(1)
fruits.pop(1)
print(fruits)

fruits.pop(0)
print(fruits)

# .sort()-> arrange in ascending order
fruits.sort()
print(fruits)

# .reverse()-> reverse the array element
fruits.reverse()
print(fruits)

