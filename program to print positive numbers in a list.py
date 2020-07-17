# program to print positive numbers in a list
'''
Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]

'''

# Example #1: Print all positive numbers from given list using for loop
#
# Iterate each element in the list using for loop and check if number is greater than or equal to 0.
# If the condition satisfies, then only print the number.

# Python program to print positive Numbers in a List

# list of numbers
list1 = [11, -21, 0, 45, 66, -93]

# iterating each number in list
for num in list1:

    # checking condition
    if num >= 0:
        print(num, end=" ")

# output : 11 0 45 66

# Example #2: Using while loop

# Python program to print positive Numbers in a List

# list of numbers
list1 = [-10, 21, -4, -45, -66, 93]
num = 0

# using while loop
while (num < len(list1)):

    # checking condition
    if list1[num] >= 0:
        print(list1[num], end=" ")

    # increment num
    num += 1

# output : 21 93

# Example #3: Using list comprehension

# Python program to print Positive Numbers in a List

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)

# output : Positive numbers in the list:  45 93

# Example #4: Using lambda expressions
# Python program to print positive Numbers in a List

# list of numbers
list1 = [-10, 21, 4, -45, -66, 93, -11]


# we can also print positive no's using lambda exp.
pos_nos = list(filter(lambda x: (x >= 0), list1))

print("Positive numbers in the list: ", *pos_nos)

# output : Positive numbers in the list:  21 4 93 

