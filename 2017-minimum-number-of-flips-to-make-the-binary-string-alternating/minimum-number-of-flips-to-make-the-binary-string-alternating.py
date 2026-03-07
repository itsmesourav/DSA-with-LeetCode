class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        d1 = d2 = x = 0
        res = n

        for r, c in enumerate(s):
            if c != "01"[r % 2]: d1 += 1
            if c != "10"[r % 2]: d2 += 1

            if r - x + 1 > n:
                if s[x] != "01"[x % 2]: d1 -= 1
                if s[x] != "10"[x % 2]: d2 -= 1
                x += 1

            if r - x + 1 == n:
                res = min(res, d1, d2)

        return res
        
        