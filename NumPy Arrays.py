#NumPy Creating Arrays
import numpy as np
arr = np.array([1, 2, 4, 6])
print(arr)

#Use a tuple to create a NumPy array:
arr = np.array((1, 4, 7, 8, 10))
print(arr)

#Create a 0-D array with value 42
ar =np.array(42)
print(ar)

#Create a 1-D array containing the values 1,2,3,4,5:
ary = np.array([1, 2, 3, 4, 5])
print(ary)

#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arry = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arry)

#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arrys = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arrys)

#Check how many dimensions the arrays have:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Create an array with 5 dimensions and verify that it has 5 dimensions:
arry = np.array([1, 2, 3, 4], ndmin = 5)
print(arry)
print('Number of dimensions :', arry.ndim)

