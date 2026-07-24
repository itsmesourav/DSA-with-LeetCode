class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0

        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)

        return ans