# coding: utf-8
def sum2(L):
    if not L:
        return 0
    else:
        return L[0] + sum2(L[1:])
        
