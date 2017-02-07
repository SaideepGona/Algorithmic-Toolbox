# Uses python3
import sys

import copy
# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10

def period_calc_sum(divisor):

    period_list = [0, 1, 2]
    tracker = [1, 2]

    while period_list[-2:] != [0, 1]:

        new_fib = (sum(tracker)+1)
        tracker[0] = tracker[1]
        tracker[1] = new_fib
        period_list.append(new_fib % divisor)

    return period_list[0:-2]


def calc_sum_last(n):

    period = period_calc_sum(10)
    period_length = len(period)
    period_index = n % period_length
    remainder = period[period_index]

    return remainder


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(calc_sum_last(n))
