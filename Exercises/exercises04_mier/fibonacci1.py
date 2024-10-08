# coding: utf-8
import sys

try:
    N = int(sys.argv[1])
except IndexError:
    N = 10

def fib1(n: int = 10) -> int:
    """
    Fibonacci numbers, recursively defined:
            fib(n) = 1, for 0 ≤ n < 2
            fib(n) = fib(n - 1) + fib(n -2), for n ≥ 2
    """
    if n < 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)
        

if __name__ == "__main__":
    for k in range(2, N + 1):
        print(f"Fibonacci number {k:<8d} {fib1(k):<20d}")
