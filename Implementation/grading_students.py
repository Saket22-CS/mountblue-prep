#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Grading Students
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):

    rounded_grades = []

    for grade in grades:

        # Grades below 38 are not rounded
        if grade < 38:
            rounded_grades.append(grade)
            continue

        # Find next multiple of 5
        next_multiple = ((grade // 5) + 1) * 5

        # Round if difference is less than 3
        if next_multiple - grade < 3:
            rounded_grades.append(next_multiple)
        else:
            rounded_grades.append(grade)

    return rounded_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()