import numpy as np

#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr.shape)

#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
aary = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(aary)
print("Print the Numpy shape:", aary.shape)

