class Solution(object):

    # using one stack only
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stk = []
        for char in S:
            if stk and stk[-1] == char:
                stk.pop()
            else:
                stk.append(char)
        return ''.join(stk)

    # using two stacks
    def removeDuplicates(self, S):
    """
    :type S: str
    :rtype: str
    """
    stk = []
    ret = []
    for item in S:
        stk.append(item)
    while stk:
        if ret and ret[-1] == stk[-1]:
            ret.pop()
            stk.pop()
        else:
            ret.append(stk.pop())
    return ''.join(list(reversed(ret)))
