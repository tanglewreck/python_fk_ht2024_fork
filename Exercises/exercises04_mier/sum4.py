# coding: utf-8
def sum4(first, *rest):
    """Must be called as sum3(*list)"""
    return first if not rest else first + sum4(*rest)
    
