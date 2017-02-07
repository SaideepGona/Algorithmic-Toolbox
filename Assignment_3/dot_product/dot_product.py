#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here

    a_num = range(len(a))
    b_num = range(len(b))

    a_sort, a_num = (list(t) for t in zip(*sorted(zip(a, a_num))))
    b_sort, b_num = (list(t) for t in zip(*sorted(zip(b, b_num))))

    total = 0

    for x in range(len(a)):

        prof = a[a_num[x]]
        clicks = b[b_num[x]]

        ad_product = prof*clicks

        total += ad_product

    return total

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
