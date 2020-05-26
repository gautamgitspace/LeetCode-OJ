#!/usr/bin/env python

"""
- begins with vowel -> append 'ma' to the end of the word
- begins with a consonant -> remove first letter and append
  at the end, then add 'ma'
- add 'a' to end of each word per its index in sentene

Example:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
"""
def goat_latin(S):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    data = S.split()
    worker = []
    result = []

    for i in range(len(data)):
        curr = data[i]
        first_alphabet = curr[0]

        if first_alphabet in vowels:
            curr += 'ma'
            worker.append(''.join(curr))
        
        elif first_alphabet not in vowels:
            curr = curr[1:] + first_alphabet + 'ma'
            worker.append(''.join(curr))

    for i, item in enumerate(worker):
        item += 'a' * (i+1)
        result.append(item)

    return result
   

if __name__ == "__main__":
    S = "I speak Goat Latin"
    print goat_latin(S)
