#!/usr/bin/python

"""
remove dups in place O(1) space, O(n) time: use below approach
detect dups can use space : use bool array approach or use HashSet
"""
def func(a):
    if not a:
        return 0
    previous = 0
    for i in range(1, len(a)):
        if a[i] != a[previous]:
            previous += 1
            a[previous] = a[i]
    return previous+1
if __name__ == "__main__":
    a = [0,1,1,2,3,4,5,5,5,5,5,5]
    print func(a)
