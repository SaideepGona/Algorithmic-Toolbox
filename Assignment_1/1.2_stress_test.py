# Uses python3

import numpy as np
import copy

count_tot = 0
count_wrong = 0

while True:

    n = np.random.randint(2, high = 11)
    a = np.random.randint(0, high = 100000, size=n)

    # n = int(input())
    # a = [int(x) for x in input().split()]
    # assert(len(a) == n)

    result = 0
    result_slow = 0
    # Slow Solution

    sorted_a = sorted(a, reverse = True)

    result_slow = int(sorted_a[0])* int(sorted_a[1])

    # FAST Solution

    # INITIALIZE the maxes. Can be optimized further

    max = 0
    max_2 = 0

    # Main loop

    for i in range(0, n):

        if a[i] >= max:

            max_2 = copy.deepcopy(max)
            max = a[i]

    result = int(max) * int(max_2)

    count_tot += 1

    if result_slow != result:

        count_wrong += 1

        print(result, result_slow)
        print(a)

    # print(result)

