# program to print even numbers in a list

'''

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]

Input: list2 = [12, 14, 95, 3]
Output: [12, 14]
'''

# Using for loop : Iterate each element in the list using for loop and check if num % 2 == 0.
# If the condition satisfies, then only print the number.

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

# output : 10 4 66

# Using while loop

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
num = 0

# using while loop
while (num < len(list1)):

    # checking condition
    if num % 2 == 0:
        print(list1[num], end=" ")

    # increment num
    num += 1

# Using list comprehension

# Python program to print even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)

# Using lambda expressions :

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]


# we can also print even no's using lambda exp.
even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)
