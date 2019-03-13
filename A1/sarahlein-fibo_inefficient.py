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

    # Function for inefficient fibonacci
    def inefficientFibonacci(n):

        if n == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        else:
            a = inefficientFibonacci(n - 1)
            b = inefficientFibonacci(n - 2)

        return a + b

    if args.all:
        result = [1, 1]
        for i in range(1, args.n + 1):
            result.append(inefficientFibonacci(args.n))
        print("Fibonacci numbers: ", result)
    else:
        print("Last Fibonacci number: ", inefficientFibonacci(args.n))

if __name__ == "__main__":
    Main()


