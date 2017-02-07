# Uses python3
import sys
import math

def binary_search(a, x):

    first = 0
    last = len(a) - 1
    found = False

    while first <= last and not found:

        midpoint = (first + last) //2

        if a[midpoint] == x:

            found = True
            return midpoint

        else:

            if x < a[midpoint]:
                last = midpoint-1

            else:
                first = midpoint+1

    null = -1

    return null

    # write your code here

# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]

    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
