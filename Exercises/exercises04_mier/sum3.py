# coding: utf-8
def sum3(L):
    return L[0] if len(L) == 1 else L[0] + sum3(L[1:])
    
