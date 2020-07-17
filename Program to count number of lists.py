# Program to count number of lists in a list of lists

'''

Input :  [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
Output : 3

Input : [[1], ['Bob'], ['Delhi'], ['x', 'y']]
Output : 4
'''


# Method #1 : Using len()

# Python3 program to Count number
# of lists in a list of lists

def countList(lst):
    return len(lst)


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(countList(lst))


# Output: 3

# Method #2 : Using type()

# Use a for loop and in every iteration to check if the type of the current item is a list or not, and accordingly increment ‘count’ variable.
# This method has a benefit over approach #1, as it works well for a list of heterogeneous elements.

# Python3 program to Count number
# of lists in a list of lists

def countList(lst):
    count = 0
    for el in lst:
        if type(el) == type([]):
            count += 1

    return count


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(countList(lst))


# Method #3 : Using isinstance() method

# Python3 program to Count number
# of lists in a list of lists

def CountList(lst):
    return sum(isinstance(i, list) for i in lst)


lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(countList(lst))
