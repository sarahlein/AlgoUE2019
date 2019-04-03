#!/usr/bin/env python3

# Manhattan Tourist Problem 2
# Sarah Meitz
# File has to be parsed as following:
# ./sarahlein-ManhattanTourist.py rmHVD_10_5
# ./sarahlein-ManhattanTourist.py rmHVD_999_5
# results: rmHVD_10_5: 53.60000000000001; rmHVD_999_5: 7203.890000000001


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
    dia = MatrixReader(matrix)

    matrix.close()

    n = len(down)
    m = len(right[0])
    s = []

# Leere Matirx wird erstellt und mit Nullen befüllt
    for j in range(0, n + 1):
        s.append([])
    for j in s:
        for i in range(0, m + 1):
            j.append(0)

    s[0][0] = 0

    for i in range(0, n):
        s[i + 1][0] = s[i][0] + down[i][0]

# Berechnung der ersten Zeile
    for j in range(0, m):
        s[0][j + 1] = s[0][j] + right[0][j]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1], s[i-1][j-1] + dia[i-1][j-1])

    #print(s[n][m])
    return s[n][m]


Main()

