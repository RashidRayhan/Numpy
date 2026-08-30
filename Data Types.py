import numpy as np
#Checking the Data Type of an Array
x = np.array([1, 2, 4, 5, 6])
print(x.dtype)

#Get the data type of an array containing strings:
y = np.array(["A", "B", "C", "12"])
print(y.dtype)

#Creating Arrays With a Defined Data Type
z = np.array([1, 2, 4, 5, 6], dtype='S')
print(z)
print(z.dtype)

#Create an array with data type 4 bytes integer:
a = np.array([1, 2, 3, 4, 5, 6], dtype = 'i4')
print(a)
print(a.dtype)

#Change data type from float to integer by using 'i' as parameter value:
b = np.array([1.2, 3.2, 4.5, 5.7])
c = b.astype('i')
print(c)
print(c.dtype)

#Change data type from float to integer by using int as parameter value:
arr = np.array([1.2, 3.5, 5.6, 7.9])
newarr = arr.astype('int')
print(newarr)

#Change data type from integer to boolean:
arry = np.array([1, 2, 4, 6])
arrys = arry.astype('bool')
print(arrys)

