import numpy as np
#Splitting NumPy Arrays

#Split the array in 3 parts:
abc = np.array([1, 2, 3, 4, 5, 6])
abs = np.array_split(abc, 3)
print(abs)

#If the array has less elements than required, it will adjust from the end accordingly.
abd = np.array([1, 2, 3, 4, 5, 6])
ads = np.array_split(abd, 4)
print(ads)

#If you split an array into 3 arrays, you can access them from the result just like any array element:
adc = np.array([1, 2, 3, 4, 5, 6])
adf = np.array_split(adc, 4)
print(adf[0])
print(adf[1])
print(adf[2])
print(adf[3])

#Use the same syntax when splitting 2-D arrays.
ads = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
abc = np.array_split(ads, 3)
print(abc)


#Split the 2-D array into three 2-D arrays.

acb = ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
adf = np.array_split(acb, 4)
print(adf)

#Split the 2-D array into three 2-D arrays along columns.
acf = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
aef = np.array_split(acf, 3, axis = 1)
print(aef)

#Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arar = np.hsplit(arr, 3)
print(arar)