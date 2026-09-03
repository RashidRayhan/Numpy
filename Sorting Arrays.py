import numpy as np

#The NumPy ndarray object has a function called sort(), that will sort a specified array.
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#Sort the array alphabetically:

num = np.array(['banana', 'cherry', 'apple'])
print(np.sort(num))

#Sort a boolean array:
arrs = np.array([True, False, True])
print(np.sort(arrs))

#If you use the sort() method on a 2-D array, both arrays will be sorted:
aar = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(aar))

