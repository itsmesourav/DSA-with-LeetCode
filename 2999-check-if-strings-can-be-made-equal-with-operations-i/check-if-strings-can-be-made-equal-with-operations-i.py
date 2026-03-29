class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a, b, c, d = s2
        return s1 in (s2,  c+b+a+d, a+d+c+b, c+d+a+b)
        #return sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and \
           #sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        