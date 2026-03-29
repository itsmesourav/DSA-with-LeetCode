class Solution(object):
    def canBeEqual(self, s1, s2):
        a, b, c, d = s2
        return s1 in (s2,  c+b+a+d, a+d+c+b, c+d+a+b)