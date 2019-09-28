from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        res = []
        d1 = Counter(text)
        d2 = Counter('balloon')

        for k, v in d1.items():
            if k in d2.keys():
                res.append(d1[k]/d2[k])
        if not res:
            return 0
        mini = min(res)
        return mini if mini !=0 and len(res) == 5 else 0
