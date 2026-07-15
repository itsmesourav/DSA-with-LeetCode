class Solution(object):
    def gcdOfOddEvenSums(self, n):
        e = 0
        o = 0

        for num in range(1, n * 2 + 1):
            if num % 2 == 0:
                e += num
            else:
                o += num
        
        def g(a, b):
            if a > b:
                return g(a - b, b)
            elif b > a:
                return g(a, b - a)
            return a

        return g(e, o)