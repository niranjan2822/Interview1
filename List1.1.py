'''

Input : list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
Output : [(1, 'a'), (2, 'b'), (3, 'c')]

Input : list1 = [1, 2, 3, 4]
        list2 = [ 1, 4, 9]
Output : [(1, 1), (2, 4), (3, 9), (4, '')]

'''


# Approach #1 : Naive

def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


# Driver code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))


# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

# Using zip() using zip() method to merge the two list elements and then typecasting into tuple.
def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list


# Driver code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))


# Output:
# ((1, 'a'), (2, 'b'), (3, 'c'))

# Approach #4 : Using enumerate(), alternative to zip().
#
# This method uses two for loops to enumerate through lists and merge the two lists.

def merge(list1, list2):
    merged_list = [(p1, p2) for idx1, p1 in enumerate(list1)
                   for idx2, p2 in enumerate(list2) if idx1 == idx2]
    return merged_list


# Driver code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))


# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

# Approach  # 5: Using map() and lambda.
# Using map() and lambda

def listOfTuples(list1, list2):
    return list(map(lambda x, y,: (x, y), list1, list2))


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(listOfTuples(list1, list2))

# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

