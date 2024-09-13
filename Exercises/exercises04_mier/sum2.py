# coding: utf-8
def sum2(L):
    first, *rest = L
    return first if not rest else first + sum2(rest)
    
