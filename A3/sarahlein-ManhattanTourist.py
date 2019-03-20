#!/usr/bin/env python3

# Manhattan Tourist Problem
# Sarah Meitz
# File has to be parsed as following:
# ./sarahlein-ManhattanTourist.py rmHV_10_5
# ./sarahlein-ManhattanTourist.py rmHV_999_5
# results: rmHV_10_5: 12.25; rmHV_999_5: 1563.4900000000098

import sys

def Main():
    file = sys.argv[1]
    score = MTP(file)
    print(score)

def MatrixReader(matrix):

    direction = []
    i = 0
    for line in matrix:
        if line.startswith(" "):
            temp = line.split()
            direction.append([])
            for number in temp:
                direction[i].append(float(number))
            i += 1
        if line.startswith("-"):
            break
    return direction


def MTP(file):
    matrix = open(file, "r")

    down = MatrixReader(matrix)
    right = MatrixReader(matrix)

    matrix.close()

    n = len(down)
    m = len(right[0])
    s = []

    for j in range(0, n + 1):
        s.append([])
    for j in s:
        for i in range(0, m + 1):
            j.append(0)

    s[0][0] = 0
    for i in range(0, n):
        s[i + 1][0] = s[i][0] + down[i][0]

    for j in range(0, m):
        s[0][j + 1] = s[0][j] + right[0][j]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]

Main()