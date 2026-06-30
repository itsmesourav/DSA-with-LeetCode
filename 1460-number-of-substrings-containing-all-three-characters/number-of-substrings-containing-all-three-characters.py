class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        fm = defaultdict(int)
        res = 0

        l = 0
        for r in range(n):
            fm[s[r]] += 1
            while l < r and all(fm[c] > 0 for c in ['a', 'b', 'c']):
                res += n - r
                fm[s[l]] -= 1
                l += 1
        
        return res