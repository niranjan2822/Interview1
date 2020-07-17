# Check if a list exists in given list of lists
'''

Given a list of lists, the task is to check if a list exists in given list of lists.

Input :
lst = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]
list_search = [4, 5, 6]

Output:  True

Input :
lst = [[5, 6, 7], [12, 54, 9], [1, 2, 3]]
list_search = [4, 12, 54]

Output:  False
'''

# Method #1: Using Counter  -> The most concise and readable way to find whether a list exists in list of lists is using
# Counter

# Python code find whether a list
# exists in list of list.
import collections

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [2, 3, 4]

# Flag initialization
flag = 0

# Using Counter
for elem in Input:
    if collections.Counter(elem) == collections.Counter(list_search):
        flag = 1

# Check whether list exists or not.
if flag == 0:
    print("False")
else:
    print("True")

# Output : True

# Method #2: Using in

# Python code find whether a list
# exists in list of list.

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [1, 1, 1, 2]

# Using in to find whether
# list exists or not
if list_search in Input:
    print("True")
else:
    print("False")
# Output : True

# Method #3: Using any

# Python code find whether a list
# exists in list of list.

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [4, 5, 6]

# Using any to find whether
# list exists or not
if any(list == list_search for list in Input):
    print("True")
else:
    print("False")

# Output : True