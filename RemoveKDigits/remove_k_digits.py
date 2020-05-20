class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str

        remove k digits from the number so that the
        new number is the smallest possible.

        use a stack and keep pushing items to it. if
        next item is less than stack top, decrement
        k and pop from stack.

        So for '1432219' and k = 3, we have:
        []
        [1]
        [1, 4]
        [1, 3] pop 4 insert 3, as 3 is lt 4. k becomes 2
        [1, 2] pop 3 insert 2, as 2 is lt 3. k becomes 1
        [1, 2, 2] continue as 2 == 2
        [1, 2, 1] pop 2 insert 1 as 1 is lt 2 k becomes 0
        [1, 2, 1, 9] don't care as k is 0
        """
        stack = []
        for idx in range(len(num)):
            while stack and k > 0:
                if num[idx] < stack[-1]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[idx])

        # cases where we don't get to decrement k
        # cause there comes on value in the string
        # which is lesser than stack top.
        # like for num = '10', k = 2 we decrement k once
        # but then k = 1 stays.
        while k != 0:
            stack.pop()
            k -= 1

        while stack:
            # leading zeroes cases such as num = '10200', k = 1
            if stack[0] == '0':
                stack = stack[1:]
            else:
                break

        return ''.join(stack) or '0'
