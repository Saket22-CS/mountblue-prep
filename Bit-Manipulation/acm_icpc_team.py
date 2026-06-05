#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: ACM ICPC Team
# Platform: HackerRank
# Difficulty: Easy
# Topic: Bit Manipulation, Strings
#
# Time Complexity: O(n² × m)
# Space Complexity: O(1)
#

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):

    maximum_topics = 0
    team_count = 0

    n = len(topic)

    for i in range(n):

        for j in range(i + 1, n):

            known_topics = 0

            for k in range(len(topic[i])):

                if topic[i][k] == '1' or topic[j][k] == '1':
                    known_topics += 1

            if known_topics > maximum_topics:

                maximum_topics = known_topics
                team_count = 1

            elif known_topics == maximum_topics:

                team_count += 1

    return [maximum_topics, team_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()