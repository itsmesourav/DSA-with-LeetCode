class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        result = 0

        for i in range(32):
            if((n >> i) & 1) > 0:
                if last >= 0:
                    result = max(result, i - last)
                last = i
        return result
        

        