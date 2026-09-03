import numpy as np

#To search an array, use the where() method.
abc = np.array([1, 2, 3, 4, 5, 4])
abs = np.where(abc == 4)
print(abs)

#Find the indexes where the values are odd:
acb = np.array([10, 14, 93, 41, 8, 7])
abf = np.where(acb % 2 == 1)
print(abf)

#Find the indexes where the values are even:
abcc = np.array([10, 14, 93, 41, 8, 7])
abg = np.where(abcc % 2 == 0)
print(abg)

#Find the indexes where the value 7 should be inserted:
abg = np.array([6, 7, 8, 9, 7])
abe = np.searchsorted(abg, 7)
print(abe)

#Find the indexes where the value 7 should be inserted, starting from the right:
abh = np.array([6, 7, 8, 9])
abd = np.searchsorted(abh, 7, side='right')
print(abd)

#Find the indexes where the values 2, 4, and 6 should be inserted:
bah = np.array([1, 3, 5, 7])
bhf = np.searchsorted(bah, [2, 4, 6])
print(bhf)