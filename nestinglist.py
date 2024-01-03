# nesting list -> list inside another list
list=[1,2,3,4,5,6,7]
list1=[5,7,3,8,3,8,3,5]
list2=[45,56,57,23,8,24,78,79]
matrix=[list,list1,list2]
print(matrix)

print(matrix[2])
print(matrix[0][3])