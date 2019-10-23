class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        """
        With extra space, obvious solution is to use
        a counter and form a new string by appending
        k, v from the counter as we go through all
        the keys

        to do it in place and O(1)  memory, we need
        pointers and a counting mechanism

        we maintain a read pointer and a write pointer
        read pointer will run until the length of the
        char array, start with first char and scan next
        chars (we move rptr forward) and if they are
        equal update the frequency, f.

        When all this is done, we start with first char
        at the wptr position and check f at each write.
        If f is greater than 1, we need to add this freq
        to the wptr position
        """

        rptr, wptr = 0, 0
        # run rptr till len of array
        while rptr < len(chars):
            # init c and f
            c, f = chars[rptr], 0
            # compare c with all elements using rptr and
            # update f on the go
            while rptr < len(chars) and chars[rptr] == c:
                rptr, f = rptr + 1, f + 1
            # now use wptr to write
            chars[wptr], wptr = c, wptr + 1
            # freq digits have their own entry
            if f > 1:
                for item in str(f):
                    chars[wptr], wptr = item, wptr + 1
        return wptr
