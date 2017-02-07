# Uses python3
import sys

def get_change(m):
    #write your code here

    five_m = m % 5
    ten_m = m % 10
    fives = 0
    tens = m //10
    ones = m % 5

    if five_m != ten_m:

        fives = 1

    sum = ones + fives + tens

    return sum

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
