class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        res = 0

        for p in patterns:
            m = len(p)
            for i in range(len(word) - m + 1):
                j = 0
                while j < m and word[i + j] == p[j]:
                    j += 1
                if j == m:
                    res += 1
                    break
        
        return res