#!/bin/python3

#
# Problem: Correctness and the Loop Invariant
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Insertion Sort, Debugging
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#

#
# Fix the bug in the insertion sort implementation.
#

def insertion_sort(l):

    for i in range(1, len(l)):

        j = i - 1
        key = l[i]

        # Fixed condition: j >= 0 instead of j > 0
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1

        l[j + 1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

insertion_sort(ar)

print(" ".join(map(str, ar)))