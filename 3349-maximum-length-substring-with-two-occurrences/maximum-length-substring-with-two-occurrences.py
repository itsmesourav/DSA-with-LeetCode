class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        fm = defaultdict(int)

        l = 0
        for r in range(n):
            fm[s[r]] += 1

            while l < r and not all(v <= 2 for v in fm.values()):
                fm[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res