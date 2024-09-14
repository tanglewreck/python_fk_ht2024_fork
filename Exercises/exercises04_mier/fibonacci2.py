# coding: utf-8
"""
Fibonacci numbers coded with a generator function
If executed on the command line, takes an integer 
argument N and produces a list of fibonacci numbers
up to the Nth number. If no argument is given,
prints the first ten fibonacci numbers.

2024-09-13
"""

import sys

# Set default maximum digits for str to int conversion
# sys.set_int_max_str_digits(100000)

try:
    args = list(map(int, sys.argv[1:]))
except ValueError as e:
    print("Non-number argument:", e)
    raise SystemExit(1)

if not args:
    args = [10]

def fib2(n: int = 10):
    """
    Fibonacci numbers, coded as a generator function 
    """
    a = [1, 1]  # First two fibonacci numbers
    for k in range(2, n + 1):
        a.append(a[k - 1] + a[k - 2])
        yield a[k]

if __name__ == "__main__":
    # Print the list of fibonacci numbers
    #print(f"Fibonacci number {0:<8d} {1:<10d}")
    #print(f"Fibonacci number {1:<8d} {1:<10d}")
    #for m, fib in enumerate(fib2(N)):
    #    print(f"Fibonacci number {m + 2:<8d} {fib:<10d}")
    for k in args:
        try:
            F = list(fib2(k))
            F_n = F[-1]
            F_n_1 = F[-2]
            print(F_n, F_n_1)
            print(F_n - F_n_1)
        except IndexError:
            pass
        except ValueError as e:
            print(e)
