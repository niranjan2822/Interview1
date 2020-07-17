# Given a list of lists, write a Python program to find the list with maximum length.
# The output should be in the form (list, list_length).
'''
# Examples:
#
# Input : [['A'], ['A', 'B'], ['A', 'B', 'C']]
# Output : (['A', 'B', 'C'], 3)
#
# Input : [[1, 2, 3, 9, 4], [5], [3, 8], [2]]
# Output : ([1, 2, 3, 9, 4], 5)

'''

# Approach #1 : Using for loop (Naive)
# This is a brute force method in which we iterate through each list item(list) and
# find the list with maximum length. Similarly, we use the for loop to find length of each list and output the maximum length.

# Python3 program to Find maximum
# length list in a nested list

def FindMaxLength(lst):
    maxList = max((x) for x in lst)
    maxLength = max(len(x) for x in lst)

    return maxList, maxLength


# Driver Code
lst = [['A'], ['A', 'B'], ['A', 'B', 'C']]
print(FindMaxLength(lst))

# Output : (['A', 'B', 'C'], 3)

# Approach #2 : Using map
# In this method we use Python map function to iterate over the inner lists to create a list of lengths,
# then get the maximum with max function.

# Python3 program to Find maximum
# length list in a nested list

def FindMaxLength(lst):
    maxList = max(lst, key=len)
    maxLength = max(map(len, lst))

    return maxList, maxLength


# Driver Code
lst = [['A'], ['A', 'B'], ['A', 'B', 'C'], ]
print(FindMaxLength(lst))


# Approach #3 : Using lambda operator
# One more method in Python to find the longest length list is the lambda operator.
# It is used for creating small, one-time and anonymous function objects in Python.
# Here we pass a variable i as argument in the len(i) expression and find the maximum length.


# Python3 program to Find maximum
# length list in a nested list

def FindMaxLength(lst):
    maxList = max(lst, key=lambda i: len(i))
    maxLength = len(maxList)

    return maxList, maxLength


# Driver Code
lst = [['A'], ['A', 'B'], ['A', 'B', 'C']]
print(FindMaxLength(lst))

