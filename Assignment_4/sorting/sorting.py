# Uses python3
import sys
import random

def partition3(a, l, r):

    pivot = a[l]
    b_wall = l
    e_wall = l

    for element in range(l, r+1):

        if a[element] == pivot:

            a[element], a[e_wall] = a[e_wall], a[element]
            e_wall += 1

        elif a[element] < pivot:

            a[element], a[b_wall] = a[b_wall], a[element]
            a[element], a[e_wall] = a[e_wall], a[element]
            e_wall += 1
            b_wall += 1

    return [b_wall, e_wall]

def partition2(a, l, r):

    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):

    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    [low_max, high_min] = partition3(a, l, r)
    randomized_quick_sort(a, l, low_max - 1);
    randomized_quick_sort(a, high_min, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
