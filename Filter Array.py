import numpy as np

#Create an array from the elements on index 0 and 2:
abc = np.array([41, 42, 43, 44])
cba = [True, False, True, False]
acb = abc[cba]
print(acb)

#Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44, 56, 70])
## Create an empty list
filter_arr = []

## go through each element in arr
for num in arr:
    if num > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new = arr[filter_arr]
print(filter_arr)
print(new)

#Create a filter array that will return only even elements from the original array:
arry = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arry = []

for num in arry:
    if num % 2 == 0:
        filter_arry.append(True)
    else:
        filter_arry.append(False)
newar = arry[filter_arry]
print(newar)

#Creating Filter Directly From Array
#Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#Create a filter array that will return only even elements from the original array:
arry = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arry = arry % 2 == 0
newary = arry[filter_arry]
print(filter_arry)
print(newary)

