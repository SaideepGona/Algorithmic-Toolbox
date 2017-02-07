# Uses python3

import timeit
import sys
import copy

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd



def gcd(a,b):

    list = [a,b]
    # list.sort(reverse = True)

    while list[1] != 0:

        remainder = list[0] % list[1]
        list[0] = list[1]
        list[1] = copy.copy(remainder)

    return list[0]

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
