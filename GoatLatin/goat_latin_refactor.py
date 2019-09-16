#!/usr/bin/env python

"""
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
        # vowels case
        if first_alphabet in vowels:
            curr += 'ma'
            worker.append(''.join(curr))
        # not vowels case
        if first_alphabet not in vowels:
            last = curr[-1]
            curr = curr[1:] + first_alphabet + 'ma'
            worker.append(''.join(curr))

    # at this point we have enverything in worker
    # convert each word to list, append a i times
    # and finally add all to result and return
    for i, item in enumerate(worker):
        curr = list(item)
        curr.append('a' * (i+1))
        result.append(''.join(curr))

    return ' '.join(result)


if __name__ == "__main__":
    S = "I speak Goat Latin"
    print goat_latin(S)
