#!/usr/bin/env python3

vowels = list('aeiouAEIOU')
res = []

def pig_latin(input):
    data = input.split()
    for i in range(len(data)):
        curr = data[i]
        first_char = curr[0]
        if first_char in vowels:
            curr += 'ay'
            res.append(curr)
        if first_char not in vowels:
            curr = curr[1:] + first_char + 'ay'
            res.append(curr)
    return res

if __name__  == "__main__":
    input = 'I am a good kid'
    print (pig_latin(input))
