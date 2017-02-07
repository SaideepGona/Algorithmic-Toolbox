# Uses python3

import numpy as np
import copy

# count_tot = 0
# count_wrong = 0
#
# while True:
#
#     n = np.random.randint(2, high = 11)
#     a = np.random.randint(0, high = 100000, size=n)

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

sorted_a = sorted(a, reverse=True)

result = int(sorted_a[0]) * int(sorted_a[1])

    # result_slow = 0
    # Slow Solution
    #
    # for i in range(0, n):
    #     for j in range(i+1, n):
    #         if a[i]*a[j] > result_slow:
    #             result_slow = a[i]*a[j]

    # FAST Solution

    # INITIALIZE the maxes. Can be optimized further

# if a[0] >= a[1]:
#
#     max = a[0]
#     max_2 = a[1]
#
# else:
#
#     max = a[1]
#     max_2 = a[0]
#
# # Main loop
#
# for i in range(2, n):
#
#     if a[i] >= max:
#
#         max_2 = copy.deepcopy(max)
#         max = a[i]
#
# result = max * max_2

    # count_tot += 1

    # if result_slow != result:
    #
    #     count_wrong += 1
    #
    #     print(result, result_slow, n)
    #
print(result)
    #
