# Uses python3
import sys
import copy

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b


def lcm(a,b):

    def gcd(a, b):

        list = [a, b]
        # list.sort(reverse = True)

        while list[1] != 0:
            remainder = list[0] % list[1]
            list[0] = list[1]
            list[1] = copy.copy(remainder)

        return list[0]

    GCD = gcd(a,b)
    a_red = a//GCD
    b_red = b//GCD
    lcm = a_red*b_red*GCD
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

