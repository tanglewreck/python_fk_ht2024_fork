# coding: utf-8

import sys

try:
    N = int(sys.argv[1])
except IndexError:
    N = 10

def fib2(n: int = 10) -> int:
    """
    Fibonacci numbers, coded as a generator function 
    """
    a = []
    a = a + [1, 1]
    for k in range(2, n + 1):
        a.append(a[k - 1] + a[k - 2])
        # print(a[k])
        yield a[k]

if __name__ == "__main__":
    print(f"Fibonacci number {0:<8d} {1:<10d}")
    print(f"Fibonacci number {1:<8d} {1:<10d}")
    for k, fib in enumerate(fib2(N)):
        print(f"Fibonacci number {k + 2:<8d} {fib:<10d}")
