class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = '0'
        curr = 0

        for c in s:
            if c != t:
                curr += 1
            t = '1' if t == '0' else '0'
                    
        res = curr
        t = '1'
        curr = 0
        for c in s:
            if c != t:
                curr += 1
            t = '1' if t == '0' else '0'
                        
        return min(res, curr)