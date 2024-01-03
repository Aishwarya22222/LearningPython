# dictionary is known as object in javascript and dictionary alwayscomes with key value pair
student={
    'first_name':'Aishwarya',
    'last_name':'Neupane',
    'age':24,
    'height':4.11,
    'subjects':['python','Django','Data Science','HTML','CSS']

}
print(student['first_name'])
print(student['age'])
print(student['subjects'][0][0])

#dictionary methods
# .keys()-> it only print key of the dictionary
print(student.keys())

# .values()-> it only print values of the dict
print(student.values())

# create a new dict( empty dict craete garera value add gareko)
d={}
d['color']='red'
# print(d)
d['brand']='carter'
print(d)

# neating with dict
nest_dict={'key1':{'nestkey':{'subnestkey':'finalvalue'}}}
print(nest_dict['key1'])
print(nest_dict['key1']['nestkey']['subnestkey'])