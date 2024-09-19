# coding: utf-8
"""
2024-09-13
Fibonacci numbers coded with a generator function

If executed on the command line, takes an integer N
as argument and produces the fibonacci sequence
up until Fibonacci number N.

If no argument is given, N defaults to 10

"""

import sys

# Set default maximum digits for str to int conversion
# sys.set_int_max_str_digits(100000)

try:
    # args = list(map(int, sys.argv[1:]))
    N = int(sys.argv[1])
except ValueError as e:
    print("Non-number argument:", e)
    raise SystemExit(1)
except IndexError:
    # args = [10]
    N = 10

#if not args:
#    args = [10]
#    N = 10

def fib2(n: int = 10):
    """
    Fibonacci numbers, coded as a generator function 
    """
    a = [1, 1]  # First two fibonacci numbers
    for k in range(2, n + 1):
        a.append(a[k - 1] + a[k - 2])
    for k in range(n + 1):
        yield a[k]

if __name__ == "__main__":
    # Print the list of fibonacci numbers
    #print(f"Fibonacci number {0:<8d} {1:<10d}")
    #print(f"Fibonacci number {1:<8d} {1:<10d}")
    #for m, fib in enumerate(fib2(N)):
    #    print(f"Fibonacci number {m + 2:<8d} {fib:<10d}")
    # print(args)
    # for k in args:
#    for k in range(2, args[0]):
#        try:
#            # Generate all Fibonacci numbers
#            # up to Fib.no. k, which is the
#            # number we seek.
#            F = list(fib2(k))
#            F_n = F[-1]
#            F_n_1 = F[-2]
#            # print(F_n, F_n_1)
#            # print(F[-1])
#            #print(F_n - F_n_1)
#        except IndexError:
#            pass
#        except ValueError as e:
#            print(e)
    F = list(fib2(N))
    print(f"Fibonacci #{N} = {F[-1]}")
    print(F)
