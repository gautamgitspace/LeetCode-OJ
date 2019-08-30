class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        We gotta reverse the string and for each char we gotta find the
        numeric equivalent. which is given by ASCII of char - 65 + 1 then
        we multiple this with 26 ^ index. keep doing for all such chars

        Sample run:

        ABC => CBA
        C => 67-65+1 = 3 multiplied by 26^0
        B => 66-65+1 = 2 multiplied by 26^1
        A => 65-65+1 = 1 multiplied by 26^2
        """

        sum = 0
        for exp, char in enumerate(reversed(s)):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum
        
