# Uses python3
import sys

def prim_calc(n):

    counts = [-1] #stores the counts leading up to the nth value. Starts at 0
    previous_values = [0] #stores the value of the step before the current index/value
    possible_precursor = float("inf")  #just used to choose the best path. is the count of the precursor value
    precursor_value = 0 #stores the value/index of the preferred path

    for value in range(1, n+1):

        possible_precursor = float("inf")
        precursor_value = 0

        if (value % 3) == 0:

            intindex3 = int(value/3)
            possible_precursor = counts[intindex3]
            precursor_value = intindex3

        if (value % 2) == 0:

            intindex2 = int(value/2)

            if counts[intindex2] < possible_precursor:

                possible_precursor = counts[intindex2]
                precursor_value = intindex2

        if counts[value-1] < possible_precursor:

            intindex1 = int(value-1)
            precursor_value = intindex1

        counts.append(counts[precursor_value] + 1)
        previous_values.append(precursor_value)

    return previous_values, counts[-1]

def backtrack(forward_track, n):

    path = []
    current_value = n

    while forward_track[current_value] !=  1:

        path.append(forward_track[current_value])
        current_value = forward_track[current_value]

    return path

def f(n):

    if n == 1:

        return [0]

    dynamic_track, length = prim_calc(n)
    the_path = backtrack(dynamic_track, n)
    the_path.append(1)
    the_path.reverse()
    the_path.append(n)    

    return the_path

'''
expath = f(2)
print(expath)
'''

input = sys.stdin.read()
n = int(input)
sequence = list(f(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
