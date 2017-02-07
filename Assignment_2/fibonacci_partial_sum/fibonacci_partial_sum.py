# Uses python3
import sys

# def fibonacci_partial_sum_naive(from_, to):
#     if to <= 1:
#         return to
#
#     previous = 0
#     current = 1
#
#     for _ in range(from_ - 1):
#         previous, current = current, previous + current
#
#     sum = current
#
#     for _ in range(to - from_):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10


def calc_sum_last_full(fib_length):

    def period_calc_sum(divisor):
        period_list = [0, 1, 2]
        tracker = [1, 2]

        while period_list[-2:] != [0, 1]:
            new_fib = (sum(tracker) + 1)
            tracker[0] = tracker[1]
            tracker[1] = new_fib
            period_list.append(new_fib % divisor)

        return period_list[0:-2]

    def calc_sum_last(n):
        period = period_calc_sum(100)
        period_length = len(period)
        period_index = n % period_length
        remainder = period[period_index]

        return remainder

    sum_digit = calc_sum_last(fib_length)

    return sum_digit

def fib_partial_sum (small,large):

    difference = (calc_sum_last_full(large) - calc_sum_last_full(small-1)) % 10

    return difference


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_partial_sum(from_, to))
