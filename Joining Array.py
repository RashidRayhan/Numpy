import numpy as np

#We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
arr1 = np.array([1, 2, 4, 5, 6])
arr2 = np.array([7, 8, 9, 10, 11, 12])
arr = np.concatenate((arr1, arr2))
print(arr)

#Join two 2-D arrays along rows (axis=1):
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])

arry = np.concatenate((arr3, arr4), axis =1)
print(arry)

#Joining Arrays Using Stack Functions
arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])

arrys = np.stack((arr5, arr6), axis = 1)
print(arrys)

#NumPy provides a helper function: hstack() to stack along rows.
arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])

arra = np.hstack((arr7, arr8))
print(arra)

#NumPy provides a helper function: vstack()  to stack along columns.
abs = np.array([1, 2, 3, 4])
abc = np.array([6, 7, 8, 9])

wxy = np.vstack((abs, abc))
print(wxy)

