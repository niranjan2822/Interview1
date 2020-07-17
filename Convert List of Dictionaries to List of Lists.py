# Convert List of Dictionaries to List of Lists

'''
Input : test_list = [{‘Gfg’: 123, ‘best’: 10}, {‘Gfg’: 51, ‘best’: 7}]
Output : [[‘Gfg’, ‘best’], [123, 10], [51, 7]]

Input : test_list = [{‘Gfg’ : 12}]
Output : [[‘Gfg’], [12]]
'''

# Method #1 : Using loop + enumerate()
# The combination of above methods can be used to perform this task.
# In this, we perform the task of iterating using loop and brute force with help of enumerate() to perform appropriate append in result list.

# Python3 code to demonstrate working of
# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()

# initializing list
test_list = [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20},
             {'Nikhil': 21, 'Akash': 30, 'Akshat': 10},
             {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]

# printing original list
print("The original list is : " + str(test_list))

# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()
res = []
for idx, sub in enumerate(test_list, start=0):
    if idx == 0:
        res.append(list(sub.keys()))
        res.append(list(sub.values()))
    else:
        res.append(list(sub.values()))

    # printing result
print("The converted list : " + str(res))

# output : The original list is : [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20}, {'Nikhil': 21, 'Akash': 30, 'Akshat': 10}, {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]
# The converted list : [['Nikhil', 'Akash', 'Akshat'], [17, 18, 20], [21, 30, 10], [31, 12, 19]]

# Method #2 : Using list comprehension

# This task can be solved in one line using list comprehension.
# In this, we extract the keys initially using keys() and values using values().

# Python3 code to demonstrate working of
# Convert List of Dictionaries to List of Lists
# Using list comprehension

# initializing list
test_list = [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20},
             {'Nikhil': 21, 'Akash': 30, 'Akshat': 10},
             {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]

# printing original list
print("The original list is : " + str(test_list))

# Convert List of Dictionaries to List of Lists
# Using list comprehension
res = [[key for key in test_list[0].keys()], *[list(idx.values()) for idx in test_list]]

# printing result
print("The converted list : " + str(res))
