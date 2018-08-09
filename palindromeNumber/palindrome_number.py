#!/usr/bin/python

def isPalindrome(x):
    y = list(str(x))
    if y[0] == "-":
        return False
    stack = []
    for element in y:
        stack.append(element)
    if y == list(reversed(stack)):
        return True
    else:
        return False
result = isPalindrome(123321)
print result
