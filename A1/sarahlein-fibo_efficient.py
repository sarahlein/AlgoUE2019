#!/usr/bin/env python3

# A1 fibonacci
# Sarah Meitz


from argparse import ArgumentParser as ap

def Main():
    # specify command line arguments
    parser = ap(description="Calculate Fibonacci numbers of given n")

    parser.add_argument("-n", type=int, default = 10, help="enter nth Fibonacci number(int), default = 10")
    parser.add_argument("--all", action="store_true", help="print all resulting Fibonacci numbers as list")

    args = parser.parse_args()

    # Function for efficient fibonacci
    def efficientFibonacci(n):
        n1 = 1
        n2 = 1
        result = [1,1]

        for i in range(2, n):
            nn = n1 + n2
            n1 = n2
            n2 = nn
            result.append(nn)

        if args.all:
            return result[:]
        else:
            return result[-1]


    if args.all:
        print("Fibonacci numbers: ", efficientFibonacci(args.n))
    else:
        print("Last Fibonacci number: ", efficientFibonacci(args.n))

if __name__ == "__main__":
    Main()

