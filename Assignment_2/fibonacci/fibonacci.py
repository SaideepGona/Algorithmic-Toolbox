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

def calc_fib(n):

    tracker = [0, 1]

    if n < 2:
        return tracker[n]

    for iter in range(2,n+1):

        new_fib = sum(tracker)
        tracker[0] = tracker[1]
        tracker[1] = copy.copy(new_fib)

    return tracker[1]

mod_list = []
for x in range(30):

    fib = calc_fib(x)
    mod_val = fib % 4
    mod_list.append(mod_val)

print(mod_list)

n = int(input())
print(calc_fib(n))
