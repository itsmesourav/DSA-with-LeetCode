class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        pos = 0

        while n:
            if (n & 1) == 0:
                res += 2**pos
            n >>= 1
            pos += 1
        return res

        