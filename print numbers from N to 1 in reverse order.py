# print numbers from N to 1 in reverse order

'''
Examples:

Input: N = 10
Output: 10 9 8 7 6 5 4 3 2 1

Input: N = 7
Output: 7 6 5 4 3 2 1
'''


# Python3 program to print all numbers
# between 1 to N in reverse order

# Recursive function to print
# from N to 1
def PrintReverseOrder(N):
    for i in range(N, 0, -1):
        print(i, end=" ");

    # Driver code


if __name__ == '__main__':
    N = 5;
    PrintReverseOrder(N);

# This code is contributed by 29AjayKumar

# output : 5 4 3 2 1

# Approach 2: We will use recursion to solve this problem.
#
# Check for the base case. Here it is N<=0.
# If base condition satisfied, return to the main function.
# If base condition not satisfied, print N and call the function recursively with value (N – 1) until base condition
# satisfies.

# Python3 program to print all numbers between 1
# to N in reverse order

# Recursive function to print from N to 1
def PrintReverseOrder(N):
    # if N is less than 1
    # then return void function
    if (N <= 0):
        return;
    else:
        print(N, end=" ");

        # recursive call of the function
        PrintReverseOrder(N - 1);

    # Driver Code


N = 5;
PrintReverseOrder(N);

# This code is contributed by Nidhi_biet
