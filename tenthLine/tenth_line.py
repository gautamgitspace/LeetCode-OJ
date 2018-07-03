#!/usr/bin/python
import os

def count_lines():
    l = []
    fname = "/Users/abhigaut/Desktop/tenth.txt"
    with open(fname) as f:
        for i,line in enumerate (f):
            l.append(line)
            pass
    if (i+1) !=10 :
        return i + 1, l[-1:]
    else:
        return i + 1, l[i]

lines, text = count_lines()
if lines < 10:
    print "file contains less than 10 lines(" + str(lines) + ")" + " Printing last line: " + "".join(text)
elif lines > 10:
    print "file contains more than 10 lines(" + str(lines) + ")" + " Printing last line: " + "".join(text)

else:
    print "10th line: " + text.rstrip()
