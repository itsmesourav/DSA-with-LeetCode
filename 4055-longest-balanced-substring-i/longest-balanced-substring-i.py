class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for left in range(len(s)):
            if len(s) - left <= res:
                break
            count = defaultdict(int)
            for right in range(left, len(s)):
                count[s[right]] += 1
                if len(set(count.values())) == 1:
                    res = max(res, right - left + 1)
        return res


        
        