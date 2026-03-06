class Solution(object):
    def checkOnesSegment(self, s):
        count = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '1':
                count += 1
                while i < n and s[i] == '1':
                    i += 1

            else:
                    i += 1

        return count <= 1
        
        