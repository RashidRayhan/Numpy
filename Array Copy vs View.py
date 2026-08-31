import numpy as np

#Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.copy()
arr[0] = 42

print(x)
print(arr)

#Make a view, change the original array, and display both arrays:
arry =np.array([1, 2, 3, 4, 5, 6])
y = arry.view()
arry[3] = 20

print(y)
print(arry)

#Make a view, change the view, and display both arrays:
aar = np.array([1, 2, 3, 4, 5, 6])
x = aar.view()
aar[2] = 20

print(aar)
print(x)

#Print the value of the base attribute to check if an array owns it's data or not:
aarra = np.array([2, 4, 6, 8, 10, 12, 14])
x = aarra.copy()
y = aarra.view()
print(x.base)
print(y.base)