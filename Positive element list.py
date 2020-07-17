# Get positive elements from given list of lists
'''
Input : [[10, -11, 222], [42, -222, -412, 99, -87]]
Output : [[10, 222], [42, 99]]

'''

# Method #1: Using Iteration

# Python code to get positive
# element from list of list

# List Initialisation
Input = [[10, -11, 222], [42, -222, -412, 99, -87]]
Output = []

# Using iteration
for elem in Input:
    temp = []
    for x in elem:
        if x > 0:
            temp.append(x)
    Output.append(temp)

# printing output
print("Initial List is :", Input)
print("Modified list is :", Output)

# output : Initial List is : [[10, -11, 222], [42, -222, -412, 99, -87]]
# Modified list is : [[10, 222], [42, 99]]

# Method #2: Using map and list Comprehension
# Python code to get positive element
# from list of list

# List Initialisation
Input = [[10, -11, 222], [42, -222, -412, 99, -87]]

# Using list comprehension and map
temp = map(lambda elem: filter(lambda a: a > 0, elem), Input)
Output = [[a for a in elem if a > 0] for elem in temp]

# printing output
print("Initial List is :", Input)
print("Modified list is :", Output)

# Method #3: Using List Comprehension

# Python code to get positive element
# from list of list

# List Initialisation
Input = [[10, -11, 222], [42, -222, -412, 99, -87]]

# Using list comprehension
Output = [[b for b in a if b > 0] for a in Input]

# printing output
print("Initial List is :", Input)
print("Modified list is :", Output)


