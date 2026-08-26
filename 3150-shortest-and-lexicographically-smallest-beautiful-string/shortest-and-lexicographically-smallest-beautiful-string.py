class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        best = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            cur = s[left:right + 1]

            if not best or len(cur) < len(best) or (
                len(cur) == len(best) and cur < best
            ):
                best = cur

        return best