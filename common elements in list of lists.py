#  Find common elements in list of lists
'''

Input : [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
Output :  [2, 3]

'''
# Method #1 : Using reduce() + lambda + set()

# This particular task can be achieved in just a one line using the combination of the above functions.
# The reduce function can be used to operate the function of “&” operation to all the list.
# The set function can be used to convert list into a set to remove repetition.

# using reduce() + lambda + set()
from functools import reduce

# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print("The original list is : " + str(test_list))

# common element extraction form N lists
# using reduce() + lambda + set()
res = list(reduce(lambda i, j: i & j, (set(x) for x in test_list)))

# printing result
print("The common elements from N lists : " + str(res))

# output : The original list is : [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
# The common elements from N lists : [2, 3]

# Method #2 : Using map() + intersection()

# The map function can be used to convert each of the lists to set to be operated by to perform the intersection,
# using the set.intersection function. This is the most elegant way to perform this particular task.

# Python3 code to demonstrate
# common element extraction form N lists
# using map() + intersection()

# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print("The original list is : " + str(test_list))

# common element extraction form N lists
# using map() + intersection()
res = list(set.intersection(*map(set, test_list)))

# printing result
print("The common elements from N lists : " + str(res)) 
