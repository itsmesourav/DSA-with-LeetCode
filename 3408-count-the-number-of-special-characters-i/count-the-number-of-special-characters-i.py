class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 0
        seen = set()

        for c in word:
            seen.add(c)

        for i in range(26):
            c = chr(i + ord('a'))
            if c in seen and c.upper() in seen:
                res += 1
        
        return res