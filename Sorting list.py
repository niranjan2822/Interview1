# Sorting list of lists with similar list elements
'''
# Output : The original list : [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]
# The list after performing sort operation : [[[1, 1], [4, 4]], [[2, 2], [3, 3], [5, 5]]]
'''

# Method #1 : Using sorted() + list comprehension
# In this method, we just use shorthand of the longer process that can be applied.
# The list is iterated and subsequent sublist is sorted using the sorted function sorting the inner list as well.

# initializing list
test_list = [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sorted()
# Sorting list of lists with similar list elements
res = [sorted(idx) for idx in test_list]

# print result
print("The list after performing sort operation : " + str(res))

# Output : The original list : [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]
# The list after performing sort operation : [[[1, 1], [4, 4]], [[2, 2], [3, 3], [5, 5]]]

# Method #2 : Using map() + sorted()

# the combination of above functions also perform the similar task as the above method,
# just the difference being that map function is used to extend the sort logic to whole of sublists.
# Sorting list of lists with similar list elements
# using map() + sorted()

# initializing list
test_list = [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]

# printing original list
print("The original list : " + str(test_list))

# using map() + sorted()
# Sorting list of lists with similar list elements
res = list(map(sorted, test_list))

# print result
print("The list after performing sort operation : " + str(res))

# output : the original list : [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]
# The list after performing sort operation : [[[1, 1], [4, 4]], [[2, 2], [3, 3], [5, 5]]]
