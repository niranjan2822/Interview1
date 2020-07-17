# Convert Key-Value list Dictionary to List of Lists --we need to perform the flattening a key value pair of dictionary
# to a list and convert to lists of list.

'''
Input: {‘gfg’: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}

Output : [[‘gfg’, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

'''

# Method #1 : Using loop + items()
# This brute force way in which we can perform this task. In this,
# we loop through all the pairs and extract list value elements using items() and render in a new list.

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()
res = []
for key, val in test_dict.items():
    res.append([key] + val)

# printing result
print("The converted list is : " + str(res))

# Output :
# The original dictionary is : {‘gfg’: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
# The converted list is : [[‘gfg’, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

# Method #2 : Using list comprehension

# This task can also be performed using list comprehension.
# In this, we perform the task similar to above method just in one-liner shorter way.

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension
res = [[key] + val for key, val in test_dict.items()]

# printing result
print("The converted list is : " + str(res))  

