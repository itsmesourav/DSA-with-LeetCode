class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        fm = Counter(word)
        res = 0
        s = sorted(fm.values(), reverse = True)

        for i, v in enumerate(s):
            res += v * (i // 8 + 1)
        
        return res