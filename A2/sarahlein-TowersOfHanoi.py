#!/usr/bin/env python3

# A2 Tower of Hanoi
# Sarah Meitz

import sys
from argparse import ArgumentParser as ap

def Main():
    # specify command line arguments
    parser = ap(description="Calculate disc moves for Tower of Hanoi problem with given number of discs. STDOUT = Movements, STDERR = Nr. of Steps")

    parser.add_argument("-n", type=int, default = 10, help="number of discs")

    args = parser.parse_args()

    def Hanoi(n, X, Y, Z):
        if n > 0:
            #global runcount
            Hanoi.runcount += 1
            Hanoi(n - 1, X, Z, Y)
            print("Move disc from tower", X, "to tower", Y)
            Hanoi(n - 1, Z, Y, X)

    Hanoi.runcount = 0
    #Hanoi(4, "X", "Z", "Y")
    Hanoi(args.n, "X", "Z" , "Y")
    #sys.stderr.write(str(Hanoi.runcount))
    print(Hanoi.runcount, file=sys.stderr)


if __name__ == "__main__":
    Main()
