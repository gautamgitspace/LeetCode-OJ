#!/usr/bin/env python3

import os
import re
import hashlib
import random
import codecs

def func(fpath):
    lines = []
    d = {}
    if os.path.exists(fpath):
        with codecs.open(fpath, mode='r', encoding='utf-8') as f:
            contents = f.read()
            # split on new line, codec above will take care of new lines
            # internal to the sentence. So whole sentence stays together
            lines = [lines.rstrip() for lines in contents.split('\n')]
            delim = re.compile(r'^%$')

            fortunes = []
            cur = []

            def save_if_nonempty(buf):
                fortune = '\n'.join(buf)
                if fortune.strip():
                    fortunes.append(fortune)

            for line in lines:
                if delim.match(line):
                    """
                    will match strings with only '%'' in them
                    keep calling save with empty curr, cause
                    we don't want just '%' to be in our
                    fortunes. The moment, we do not match
                    just '%' and match an actual line, we add
                    it to cur
                    """
                    save_if_nonempty(cur)
                    cur = []
                    continue
                cur.append(line)

            if cur:
                # actual line, so curr won't be empty here
                save_if_nonempty(cur)

            for item in fortunes:
                hash = hashlib.md5(item.encode('utf-8')).hexdigest()
                d[hash] = item
    return d


if __name__ == "__main__":
    fpath = '/Users/gautam/Desktop/fortunes'
    d = func(fpath)
    print (''.join((d[random.choice(list(d))])))
