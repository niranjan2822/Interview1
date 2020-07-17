# Uncommon elements in Lists of List

'''

Input: The original list 1 : [[1, 2], [3, 4], [5, 6]]
output : [[3, 4], [5, 7], [1, 2]]
# The uncommon of two lists is : [[5, 6], [5, 7]]

'''

# Method 1 : Naive Method

# This is the simplest method to achieve this task and uses the brute force approach of executing a loop and to check
# if one list contains similar list as of the other list, not including that.

# using naive method

# initializing lists
test_list1 = [[1, 2], [3, 4], [5, 6]]
test_list2 = [[3, 4], [5, 7], [1, 2]]

# printing both lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using naive method
# Uncommon elements in List
res_list = []
for i in test_list1:
    if i not in test_list2:
        res_list.append(i)
for i in test_list2:
    if i not in test_list1:
        res_list.append(i)
# printing the uncommon
print("The uncommon of two lists is : " + str(res_list))

# OUTPUT : The original list 1 : [[1, 2], [3, 4], [5, 6]]
# The original list 2 : [[3, 4], [5, 7], [1, 2]]
# The uncommon of two lists is : [[5, 6], [5, 7]]

# Method 2 : Using set() + map() and ^
# The most efficient and recommended method to perform this task is using the combination of set() and map() to achieve it.
# Firstly converting inner lists to tuples using map, and outer lists to set,
# use of ^ operator can perform the set symmetic difference and hence perform this task.
# Further if it is required to get in lists of list fashion, we can convert outer and inner containers back to list using map().

# Uncommon elements in Lists of List
# using map() + set() + ^

# initializing lists
test_list1 = [[1, 2], [3, 4], [5, 6]]
test_list2 = [[3, 4], [5, 7], [1, 2]]

# printing both lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using map() + set() + ^
# Uncommon elements in Lists of List
res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
res_list = list(map(list, res_set))

# printing the uncommon
print("The uncommon of two lists is : " + str(res_list))

