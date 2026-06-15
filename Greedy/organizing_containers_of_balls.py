#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Organizing Containers of Balls
# Platform: HackerRank
# Difficulty: Medium
# Topic: Greedy, Matrix
#
# Time Complexity: O(n²)
# Space Complexity: O(n)
#

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):

    n = len(container)

    # Total balls in each container
    container_capacity = [sum(row) for row in container]

    # Total balls of each type
    ball_count = [0] * n

    for j in range(n):
        for i in range(n):
            ball_count[j] += container[i][j]

    container_capacity.sort()
    ball_count.sort()

    return "Possible" if container_capacity == ball_count else "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()