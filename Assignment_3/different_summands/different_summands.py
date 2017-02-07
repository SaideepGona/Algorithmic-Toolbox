# Uses python3
import sys

def optimal_summands(n):

    summands = []
    #write your code here

    l = 1
    k = n

    if k == 1:

        return [1]

    while k >= (2*l + 1):

        summands.append(l)
        k = k - l
        l += 1

    summands.append(k)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
