# Uses python3
import sys

def get_optimal_value(capacity, weights, values):

    value = 0.
    length_of_stuff = len(weights)

    # write your code here
    ratios = []
    for x in range(length_of_stuff):

        ratio_x = values[x] / weights[x]
        ratios.append(ratio_x)

    # Sorts lists in a zip fashion
    ratios, weights, values = (list(t) for t in zip(*sorted(zip(ratios, weights, values), reverse=True)))

    # Main Logic

    if len(weights) == 1:

        if weights[0] <= capacity:

            value = values[0]

        if weights[0] > capacity:

            proportion = (capacity/ weights[0])
            value = value + (proportion * values[0])

        return value

    while capacity != 0:

        if weights[0] <= capacity:

            value += values[0]
            del values[0]

            capacity = capacity - weights[0]
            del weights[0]

        elif weights[0] > capacity:

            proportion = (capacity/weights[0])

            value = value + (proportion * values[0])

            return value

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
