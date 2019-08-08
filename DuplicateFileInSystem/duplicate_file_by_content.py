#!/usr/bin/python

input = ["root/a 1.txt(abcdr) 2.txt(efghr)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efghr)", "root 4.txt(efgh)"]
d = {}
res = []
for items in input:
    tokens = items.split(" ")
    dir = tokens[0]
    file_names = tokens[1:]

    for items in file_names:
        file_content = items.split("(")[1].strip(")")
        d.setdefault(file_content, []).append(dir + "/" + items.split("(")[0])

for keys, values in d.items():
    if len(values) > 1:
        res.append(values)

print res
