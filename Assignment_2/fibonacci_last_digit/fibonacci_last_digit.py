# Uses python3

import copy

# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))

def calc_fib_list(n):

    tracker = [0, 1]

    if n < 2:
        return tracker[n]

    for iter in range(2,n+1):
        new_fib = (sum(tracker)) % 10
        tracker[0] = tracker[1]
        tracker[1] = copy.copy(new_fib)
    return tracker[1]

n = int(input())
print(calc_fib_list(n))
