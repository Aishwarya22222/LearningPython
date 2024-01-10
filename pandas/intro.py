# pandas is a python library used to analyze the data.
# to install pandas : pip install pandas

import pandas as pd

data={
    'fruits':['Apple','Banana','Kiwi','Guava'],
    #'color':['red','purple','green','pink']
    'quantity':['1kg','halfdozen','2kg','3kg']
}
result=pd.DataFrame(data,index=['sun','mon','tue','wed'])
print(result)

data1=[1,2,3,4,5,7,7]
print(pd.Series(data1))
print(pd.DataFrame(data1))

# labels
result1=pd.Series(data1,index=('a','b','c','d','e','f','g'))
print(result1)

# dict
student={
    'first_name':'Aishwarya',
    'last_name':'Neupane',
    'roll_no':'02'
}
print(pd.Series(student))

