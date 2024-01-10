# numpy is used to work with array data in python

#pip install numpy(To install numpy)

# 1D array
import numpy as np

arr=np.array([1,2,3,4,4,5,6])
print(arr)
print(type(arr))

# 2D array
ndarr=np.array([[1,2,3,4,],[5,6,7,8]])
print(ndarr)

# 3D array
ndarrr=np.array([[[1,3,4,5,6],[4,3,5,6,6]],[[2,4,5,6,7],[3,4,5,6,7]]])
print(ndarrr)

# 0D array
ndar=np.array(20)
print(ndar)
print(type(ndar))


# indexing
print(arr[0]) #1D
print(arr[2:4])

print(ndarr[1][2])#2D

print(ndarrr[0][1][3])#3D

# data types in numpy
# i-> integer
# b-> boolean
# f-> float
# m-> timedelta
# s-> string
# o-> object
# u-> unicode string
# M-> datetime
# numpy has a method dtype to return the data type of numpy array.

print(arr.dtype)

# random
from numpy import random
result=random.randint(50,size=(5,7))
print(result)

# distribution
from numpy import random
dist=random.choice([1,5,8,10],p=[0.2,0.4,0.4,0],size=(15)) # 1D array
print(dist)

dist1=random.choice([1,5,8,10],p=[0.2,0.4,0.4,0],size=(2,4)) # 2D array
print(dist1)

dist2=random.choice([1,5,8,10],p=[0.2,0.4,0.4,0],size=(1,2,3,4)) # 3D array
print(dist2)

#pip install seaborn

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([1,2,3,4,5,6,7])
plt.show()




