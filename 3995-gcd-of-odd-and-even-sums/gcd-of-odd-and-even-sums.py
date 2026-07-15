class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e = 0
        o = 0
        for num in range(1, n * 2 + 1):
            if num % 2 == 0:
                e += num
            else:
                o += num
        return gcd(e, o)