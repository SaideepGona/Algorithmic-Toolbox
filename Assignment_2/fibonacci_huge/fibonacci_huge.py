# Uses python3
import sys
import copy
# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m

def period_calc(divisor):

    period_list = [0, 1, 1]
    tracker = [1, 1]

    while period_list[-2:] != [0, 1]:

        new_fib = sum(tracker)
        tracker[0] = tracker[1]
        tracker[1] = new_fib
        period_list.append(new_fib % divisor)

    return period_list[0:-2]

def get_fib_huge(n,m):

    period = period_calc(m)
    period_length = len(period)
    period_index = n % period_length
    remainder = period[period_index]

    return remainder



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fib_huge(n, m))





