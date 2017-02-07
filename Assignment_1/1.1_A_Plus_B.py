# python3

# Assignment 1 Week 1: "A plus B"

# Problem Description *************************

# Problem. Given two digits a and b, find a+b.

# Input format. The first line of the input contains two integers a and b (separated by a space).

# Constraints. 0≤a,b≤9.

# Output format. Output a+b. ******************

# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys

while True:
    try:
        my_input = input("Enter two numbers with a space in between. Press Ctrl+c to quit.\n> ")
        # my_input = sys.stdin.read()
        tokens = my_input.split()
        a = int(tokens[0])
        b = int(tokens[1])
        print(a + b)
    except (ValueError, IndexError):
        print ("You didnt enter a pair of numbers, you nub")
        continue
