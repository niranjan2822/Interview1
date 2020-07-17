# Subtract two list elements if element in first list is greater

'''
Given two list, If element in first list in greater than element in second list, then subtract it, else return the element of first list only.

Examples:

Input:
l1 = [10, 20, 30, 40, 50, 60]
l2 = [60, 50, 40, 30, 20, 10]
Output:
[10, 20, 30, 10, 30, 50]

Input:
l1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
l2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output:
[6, 5, 5, 20, 23, 52, 5, 4, 9]

'''

# Method 1: The naive approach is to traverse both list simultanously and if the element in first list in greater than
# element in second list, then subtract it, else if the element in first list in smaller than element in second list,
# then return element of first list only.

# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.

# Input list initialisation
Input1 = [10, 20, 30, 40, 50, 60]
Input2 = [60, 50, 40, 30, 20, 10]

# Output list initialisation
Output = []

for i in range(len(Input1)):
    if Input1[i] > Input2[i]:
        Output.append(Input1[i] - Input2[i])
    else:
        Output.append(Input1[i])

print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)

# Output : Original list are :
# [10, 20, 30, 40, 50, 60]
# [60, 50, 40, 30, 20, 10]
#
# Output list is
# [10, 20, 30, 10, 30, 50]

# Method 2: Using zip() we subtract if element in first list is greater than element in second list,
# else we output element of first list.

# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.

# Input list initialisation
Input1 = [10, 20, 30, 40, 50, 60]
Input2 = [60, 50, 40, 30, 20, 10]

# using zip()
Output = [e1 - e2 if e1 > e2 else e1 for (e1, e2) in zip(Input1, Input2)]

# Printing output
print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)

# Method 3: Using list comprehension.


# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.

# Input list initialisation
Input1 = [10, 20, 30, 40, 50, 60]
Input2 = [60, 50, 40, 30, 20, 10]

# Output list initialisation
Output = [Input1[i] - Input2[i] if Input1[i] > Input2[i] \
              else Input1[i] for i in range(len(Input1))]

# Printing output
print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)

# Method 4: Using numpy() to complete the above task.

# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.


import numpy as np

# Input list initialisation
Input1 = np.array([10, 20, 30, 40, 50, 60])
Input2 = np.array([60, 50, 40, 30, 20, 10])

# using numpy
Output = np.where(Input1 >= Input2, Input1 - Input2, Input1)

# Printing output
print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)


#

Input1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
Input2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

# Output list initialisation
Output = []

for i in range(len(Input1)):
    if Input1[i] > Input2[i]:
        Output.append(Input1[i] - Input2[i])
    else:
        Output.append(Input1[i])

print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)

# output : Original list are :
# [15, 9, 10, 56, 23, 78, 5, 4, 9]
# [9, 4, 5, 36, 47, 26, 10, 45, 87]
#
# Output list is
# [6, 5, 5, 20, 23, 52, 5, 4, 9]


