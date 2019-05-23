#!/usr/bin/python

"""
key is sort the words in the list. Once this is done, the first
and the last words will be the most sorted ones. Then just compare
the alphabets one by one until we hit a different one.

python do how - accessing alphabets of word at 0 index in the list
by indices - list[0][i]
"""

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def dump(self):
        for items in self.items:
            print items

    def sort(self):
        return sorted(self.items)

    def longest_prefix(self):
        str = ""
        if not self.items:
            return str
        sorted_list = sorted(self.items)
        for i in range(0, min(len(sorted_list[0]), len(sorted_list[-1]))):
            if sorted_list[0][i] == sorted_list[-1][i]:
                str += sorted_list[0][i]
            else:
                break
        return str

if __name__ == "__main__":
    list = ["abc", "abcd", "abcde", "acbdhj"]
    stack = Stack()
    for items in list:
        stack.push(items)
    print stack.longest_prefix()
