class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        allnumsxor = nums[0]
        """
        this will basically give
        us the xor of those two
        target nums which appear
        just once in nums
        
        note that for 2 nums to
        be different, they differ
        in their some set bit posi
        otherwise their XOR would
        be 0
        
        Here let's say that diff
        bit is the i th bit and 
        can be found by using a
        bit_set and ANDing with
        allnumsxor
        """
        bit_set = 1
        
        for num in nums[1:]:
            allnumsxor ^= num
        
        while (allnumsxor & bit_set) == 0:
            bit_set <<= 1
        
        """
        now we know that ith posi
        now since all number occur
        twice and 2 numbers occur
        once, these numbers can be
        divided into groups where
        one group has ith bit set
        as 0 and other has ith bit
        set as 1
        
        in this case these groups
        are:
        
        G1 (1,1,5) with i = 2
        001,001,101 => 2nd bit is 0
        G2 (2,2,3) with i = 2
        010,010,110 => 2nd bit is 1
        
        since we know the diff bit
        posi is 2, from above, we
        take each num and check
        in which G it falls.
        
        For a num to fall in G1 we
        want to check if bit 2 is 0
        so we AND 2 with the num and
        expect 0 to be the output
        
        For a num to fall in G2 we
        want to check if bit 2 is 1
        so we AND 2 with the num and
        expect 1 to be the output
        
        Once we know which belongs
        where, we just xor them all
        as this by nature of numnber
        distribution, bound to have
        1 unique numer. This way we
        find both n1 and n2
        """
        n1, n2 = 0, 0
        for num in nums:
            if num & bit_set:
                n1 ^= num
            else:
                n2 ^= num

        return [n1, n2]
