class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        
        x = []
        sm = 0

        for c in str(n):
            if c != '0':
                x.append(c)
                sm += int(c)

        return int("".join(x)) * sm 