import numpy as np

#Convert the following 1-D array with 12 elements into a 2-D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr = arr.reshape(2, 5)
print(newarr)

#Convert the following 1-D array with 12 elements into a 3-D array.
arry = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarry = arry.reshape(3, 3)
print(newarry)

#Check if the returned array is a copy or a view:
ara = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(ara.reshape(2, 4).base)

#Convert 1D array with 8 elements to 3D array with 2x2 elements:
aray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newaray = aray.reshape(2, 2, -1)
print(newaray)

#Convert the array into a 1D array:
arra = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arra.reshape(-1)
print(newarr)

