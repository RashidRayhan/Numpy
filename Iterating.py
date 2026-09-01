import numpy as np
#Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3, 4, 5])
for x in arr:
    print(x)

#Iterate on the elements of the following 2-D array:
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for y in arr2d:
    print(y)

#Iterate on each scalar element of the 2-D array:
arrd = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in arrd:
    for y in x:
        print(y)

#Iterate on the elements of the following 3-D array:
arr3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
for x in arr3d:
    print(x)

#Iterate on each scalar element of the 3-D array
arr3da = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
for x in arr3da:
    for z in x:
        for y in z:
            print(y)

#Iterate through the following 3-D array:
arr3i = np.array([[[1, 2, 3], [5, 6, 7]], [[9, 10, 11], [13, 14, 15]]])
for x in np.nditer(arr3i):
    print(x)

"""NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
"""
arrin = np.array([1, 2, 3])
for x in np.nditer(arrin, flags=['buffered'], op_dtypes=['S']):
    print(x)

#Iterate through every scalar element of the 2D array skipping 1 element:
arrs = np.array([[1, 2, 3], [4, 5, 6]])
for y in np.nditer(arrs[:, ::2]):
    print(y)

#Enumerate on following 1D arrays elements:
arrn = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arrn):
    print(idx, x)

#Enumerate on following 2D array's elements:
arr2n = np.array([[1, 2, 3], [4, 5, 6]])
for idx, x in np.ndenumerate(arr2n):
    print(idx, x)