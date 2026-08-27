import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[1 : 3])

#Slice elements from index 4 to the end of the array:
arrs = np.array([1, 2, 4, 5, 6, 7, 8])
print(arrs[2:])

#Slice elements from the beginning to index 4 (not included):
arry = np.array([2, 4, 6, 8, 10, 12])
print(arry[: 5])

#Negative Slicing
arrn = np.array([1, 2, 4, 5, 6, 7, 8])
print(arrn[-5 : -1])

#Use the step value to determine the step of the slicing:
arry = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arry[1 : 7 : 4])

#Return every other element from the entire array:
arar = np.array([1, 2, 3, 4, 5, 6, 7])
print(arar[::6])

#Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(arr[1, 1:3])

#From both elements, return index 2:
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(arr[0:2, 2])

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(arr1[ 0:3, 1:2])