# write a Python program to convert each element of the given list into a sublist.
# Thus, converting the whole list into a list of lists.

'''
Examples:

Input : ['alice', 'bob', 'cara']
Output : [['alice'], ['bob'], ['cara']]

Input : [101, 202, 303, 404, 505]
Output : [[101], [202], [303], [404], [505]]
'''

# Approach #1 : Naive Approach

# Use another list ‘res’ and a for a loop. Using split() method of Python we extract each element from the list
# in the form of the list itself and append it to ‘res’. Finally, return ‘res’.
# One drawback of this method is that it does not work with integer list as ‘int’ object has no attribute ‘split’.

# Python3 program to convert
# list into a list of lists

def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)

    return (res)


# Driver code
lst = ['alice', 'bob', 'cara']
print(extractDigits(lst))

# Output : [['alice'], ['bob'], ['cara']]

# Approach #2 : List comprehension

# List comprehension is an efficient approach as it doesn’t make use of extra space.
# For each element ‘el’ in list, it simply appends [el] to the output list.

# Python3 program to convert
# list into a list of lists

def extractDigits(lst):
    return [[el] for el in lst]


# Driver code
lst = ['alice', 'bob', 'cara']
print(extractDigits(lst))

# Approach #3 : Python map()

# The given code maps the function el:[el] for each item of the given iterable ‘lst’. Hence outputs
# each element as a list itself.


# Python3 program to convert
# list into a list of lists

def extractDigits(lst):
    return list(map(lambda el: [el], lst))


# Driver code
lst = ['alice', 'bob', 'cara']
print(extractDigits(lst)) 