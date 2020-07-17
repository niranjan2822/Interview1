# Ways to sum list of lists and return sum list

'''
Input-  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output -  [12, 15, 18]
'''

# Method # 1: Using Naive method
# Python code to demonstrate
# sum of list of list
# using naive method

# Declaring initial list of list
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Printing list of list
print("Initial List - ", str(L))

# Using naive method
res = list()
for j in range(0, len(L[0])):
    tmp = 0
    for i in range(0, len(L)):
        tmp = tmp + L[i][j]
    res.append(tmp)

# printing result
print("final list - ", str(res))

# output : Initial List -  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# final list -  [12, 15, 18]

# Method #2: Using numpy array

# A numpy is a general-purpose array-processing package.
# It provides a high-performance multidimensional array object, and tools for working with these arrays.
# Python code to demonstrate
# sum of list of list
# using numpy array functions
import numpy as np

# Declaring initial list of list
List = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Printing list of list
print("Initial List - ", str(List))

# Using numpy sum
res = np.sum(List, 0)

# printing result
print("final list - ", str(res))

# Output :
# Initial List -
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# final list -  [12 15 18]

# Method #3: Using zip() and list comprehension

# Python code to demonstrate
# sum of list of list using
# zip and list comprehension

# Declaring initial list of list
List = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# Printing list of list
print("Initial List - ", str(List))

# Using list comprehension
res = [sum(i) for i in zip(*List)]

# printing result
print("final list - ", str(res))

