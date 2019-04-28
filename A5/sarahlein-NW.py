#!/usr/bin/python3

# A5 Needleman-Wunsch algorithm for global alignment of two sequences
# Sarah Meitz

from Bio import SeqIO
import sys
from sys import stdin
from argparse import ArgumentParser as ap

parser = ap(description="Needleman-Wunsch (NW) algorithm for global alignment of two sequences")

parser.add_argument("-match", type=int, default = 1, help="Enter matching score for sequence alignment, default = 1")
parser.add_argument("-mismatch", type=int, default = -1, help="Enter mismatching score for sequence alignment, default = -1")
parser.add_argument("-gap", type=int, default = -2, help="Enter gap penalty, default = -2")

args = parser.parse_args()


def readFasta():
    seqIDs = []
    seqs = []
    for Sequence in SeqIO.parse(stdin, "fasta"):
        seqIDs.append(str(Sequence.id))
        seqs.append(str(Sequence.seq).lower())

    seq1 = seqs[0]
    seq2 = seqs[1]
    seqID1 = seqIDs[0]
    seqID2 = seqIDs[1]

    return seq1, seq2, seqID1, seqID2
    

def score_match():
    return args.match
def score_mismatch():
    return args.mismatch
def score_gap():
    return args.gap

def score_comp(pos1, pos2):
    if pos1 == pos2:
        return score_match()
    if pos1 == '-' or pos2 == '-':
        return score_gap()
    return score_mismatch()

# build similarity matrix
def similarity(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # empty matrix
    score = []
    for j in range(0, m + 1):
        score.append([])
    for j in score:
        for i in range(0, n + 1):
            j.append(0)

    # build scores, fill matrix
    for i in range(0, m + 1):
        score[i][0] = score_gap() * i
    for j in range(0, n + 1):
        score[0][j] = score_gap() * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + score_comp(seq1[i - 1], seq2[j - 1])
            delete = score[i - 1][j] + score_gap()
            insert = score[i][j - 1] + score_gap()
            score[i][j] = max(match, delete, insert)

    return score

def alignment(seq1, seq2, score):
    i = len(seq1)
    j = len(seq2)
    s_align = ""
    t_align = ""

    while True:
        if i == 0 and j == 0:
            break

        if j == 0:
            s_align += seq1[i - 1]
            t_align += '-'
            i -= 1
            continue

        if i == 0:
            s_align += '-'
            t_align += seq2[j - 1]
            j -= 1
            continue

        if score[i][j] == score[i-1][j] + score_gap():
            s_align += seq1[i-1]
            t_align += '-'
            i -= 1

        elif score[i][j] == score[i][j-1] + score_gap():
            s_align += '-'
            t_align += seq2[j - 1]
            j -= 1

        elif score[i][j] == score[i-1][j-1] + score_comp(seq1[i-1], seq2[j-1]):
            s_align += seq1[i-1]
            t_align += seq2[j-1]
            i -= 1
            j -= 1

    return s_align, t_align


def calculate(s_align, t_align):
    # reverse sequences
    s_align = s_align[::-1]
    t_align = t_align[::-1]

    # calculate identity, score and aligned sequences
    score = 0
    identity = 0

    for i in range(0, len(s_align)):
        # check match
        if s_align[i] == t_align[i]:
            identity += 1
            score += score_comp(s_align[i], t_align[i])

        # check gap
        elif s_align[i] != t_align[i] and s_align[i] != '-' and t_align[i] != '-':
            score += score_comp(s_align[i], t_align[i])

        # other missmatch
        else:
            score += score_gap()

    identity = float(identity) / len(s_align) * 100

    return identity, score

def print_results(identity, score):
    #print("identity: %3.3f " % identity + "%", file=sys.stderr)
    #print("score: ", score, file=sys.stderr)
    print(score, file=sys.stderr) # ourput score to stdterror


def nmw(seq1, seq2, seqID1, seqID2):
    score = similarity(seq1, seq2)
    s_align, t_align = alignment(seq1, seq2, score)
    stars = ""
    for i in range(0, len(s_align)):
        if s_align[i] is t_align[i]:
            stars += "*"
        else:
            stars += " "
    s = s_align[::-1]
    t = t_align[::-1]
    stars_rev = stars[::-1]
    rows = len(seq1) / 60 # calculate needed rows
    print("CLUSTAL\n")
    for i in range(1, int(rows) + 2):
        if i == int(rows) + 2 and rows > int(n):
            print(seqID1, "\t", s[60 * (i - 1)::])
            print(seqID2, "\t", t[60 * (i - 1)::])
            print("".ljust(len(seqID1)), "\t", stars_rev[60 * (i - 1)::], "\n")
            break
        print(seqID1, "\t", s[60 * (i - 1):60 * i])
        print(seqID2, "\t", t[60 * (i - 1):60 * i])
        print("".ljust(len(seqID1)), "\t", stars_rev[60 * (i - 1):60 * i], "\n")

    identity, score = calculate(s_align, t_align)

    print_results(identity, score)


if __name__ == "__main__":


    seq1, seq2, seqID1, seqID2 = readFasta()

    nmw(seq1, seq2, seqID1, seqID2)
