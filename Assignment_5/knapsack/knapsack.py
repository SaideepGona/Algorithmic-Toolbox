# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    w.sort()
    w = [0] + w
    WwTable = np.zeros((len(w), W+1))
    bar_index = 1

    for bar_index in range(1, len(w)):

        for knapsack in range(1,W+1):

            WwTable[bar_index, knapsack] = WwTable[bar_index-1, knapsack]

            if w[bar_index] <= knapsack:

                val = WwTable[bar_index - 1, knapsack-w[bar_index]] + w[bar_index]

                if WwTable[bar_index, knapsack] < val:

                    WwTable[bar_index, knapsack] = val

    final = int(max(WwTable[:,W]))

    return final
'''
knap = 16

bars = [10,5,4,2]

x = optimal_weight(knap, bars)

print (x)

'''
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

'''

                current_weight = w_i

                if bar_index == 1:
                    prev = 0
                else:
                    prev = np.amax(WwTable[0:bar_index - 1,knapsack - w_i])

                current_weight = current_weight + prev

            else:

                current_weight = WwTable[bar_index - 1,knapsack]

            WwTable[bar_index,knapsack] = current_weight

        bar_index = bar_index + 1
'''