#Convert List of lists to list of Strings
'''

Input : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
Output: ['gfg', 'is', 'best']
'''

# Method #1 : Using list comprehension + join()
# The combination of above functionalities can be used to perform this task.
# In this, we perform the task of iteration using list comprehension and join() is used to perform task of joining string to list of strings

# Python3 code to demonstrate working of
# Convert List of lists to list of Strings
# using list comprehension + join()

# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]

# printing original list
print("The original list : " + str(test_list))

# Convert List of lists to list of Strings
# using list comprehension + join()
res = [''.join(ele) for ele in test_list]

# printing result
print("The String of list is : " + str(res))

# Output : The original list : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
# The String of list is : ['gfg', 'is', 'best']

# Method #2: Using map() + join()
# The task above can also be performed using combination of above methods.
# In this, we perform the task of conversion using join and iteration using map().

# Python3 code to demonstrate working of
# Convert List of lists to list of Strings
# using map() + join()

# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]

# printing original list
print("The original list : " + str(test_list))

# Convert List of lists to list of Strings
# using map() + join()
res = list(map(''.join, test_list))

# printing result
print("The String of list is : " + str(res))

