#!/usr/bin/python

"""
idea is to maintain a list called 'out' which will store the resultant path
and dirs. whereever and whenever we wanna 'up onr dir' based on '..', we pop from out.
"""

class Solution(object):
    def simplify_path(self, path):
        if not path:
            return None
        slist = path.split('/')
        out = []
        for i in slist:
            if i:
                # UP ONE DIR
                if i == "..":
                    if out:
                        print "popping cherry: " + out.pop()
                elif i == ".":
                    continue
                else:
                    print "appending " + i
                    out.append(i)
        return "/" + "/".join(out)

if __name__ == "__main__":
    path = "/a/./b/../../c/"
    sol = Solution()
    print sol.simplify_path(path)
