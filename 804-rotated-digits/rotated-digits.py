class Solution:
    def rotatedDigits(self, n: int) -> int:
        rot = {
            '0' : '0',
            '1' : '1',
            '8' : '8',
            '2' : '5',
            '5' : '2',
            '6' : '9',
            '9' : '6'
        }

        res = 0
        for num in range(1, n + 1):
            s = str(num)
            ns = ''
            for c in s:
                if not c in rot:
                    break
                ns += rot[c]
            if len(ns) == len(s) and ns != s:
                res += 1
        return res