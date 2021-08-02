import numpy as np
data = np.random.randn(2, 3)
print(data,"\n\n",data*8,"\n\n",data+data,"\n\nThe data shape is:",data.shape,"\nThe data type is:", data.dtype)

#creating ndarrays
data1=[6,8,10,12]
arr1=np.array(data1)
print("Creating ndarrays\n",arr1)

#Nested lists are converted into a multidimenional array
data2=[[1,3,5,7,9],[1,2,3,4,5]]
arr2 = np.array(data2)
print("multidimensional array\t","\nShape=",arr2.shape,"\nThe dimensions are =",arr2.ndim,"\nThe type is=",arr2.dtype)
#empty array
print(np.zeros(8), "\nZeroes array: ",np.zeros((3, 6))," \nRandom array:" ,np.empty((2, 3, 2)), "\nUsing arange: ",np.arange(15))
#Specifying a particular type of data while creating an array
print(np.array([1, 2, 3]), dtype=np.float64)
print("\n Input data with condition type as int32:", np.array([1, 2, 3]), dtype=np.int32)




