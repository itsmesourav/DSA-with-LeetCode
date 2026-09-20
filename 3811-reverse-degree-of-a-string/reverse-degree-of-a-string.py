class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i in range(len(s)):
            reverse_value = 26 - (ord(s[i]) - ord('a'))
            position = i + 1

            ans += reverse_value * position

        return ans