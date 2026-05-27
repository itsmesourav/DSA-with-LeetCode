class Solution(object):
    def numberOfSpecialChars(self, word):
        n = len(word)
        lastlower = {}
        firstupper = {}

        for i, c in enumerate(word):
            if c.islower():
                lastlower[c] = i
            elif not c in firstupper:
                firstupper[c] = i
        
        res = 0
        for i in range(26):
            c = chr(i + ord('a'))
            if (
                c in lastlower and
                c.upper() in firstupper and
                lastlower[c] < firstupper[c.upper()]
            ):
                res += 1
        return res