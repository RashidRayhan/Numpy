#The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 import
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

#Get the second element from the following array.
arr = np.array([1, 2, 3, 4, 5])
print(arr[1])

arry = np.array([1, 2, 3, 4, 5, 6])
print(arry[2] + arry[3] + arry [4])

#Access 2-D Arrays
arrys = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element on 1st row: ", arrys[0, 2])

#2nd row result in 2D arrays
arra = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element on 2nd row: ", arra[1, 3])

#Access 3-D Arrays
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(arr[0, 1, 2])

#Negative Indexing
arrs = np.array([[1, 2, 3], [4, 5, 6]])
print(arrs[1, -1])

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])