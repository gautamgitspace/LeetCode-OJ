#!/usr/bin/env python
#LEETCODE OJ PROBLEM 3
def longest_substr(text):
    #MAP {KEY = CHARACTER, VALUE = INDEX}
    distinguisher = {}
    left = -1
    longest = 0
    for i, alphabet in enumerate (text):
        if alphabet in distinguisher and distinguisher.get(alphabet) > left:
            left = distinguisher.get(alphabet)
        longest = max(longest, i-left)
        distinguisher[alphabet] = i
    return longest

print longest_substr("pwwkew")
