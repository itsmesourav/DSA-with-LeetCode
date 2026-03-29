class Solution(object):
    def canBeEqual(self, s1, s2):
        # check positions 0 and 2
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
    
        # check positions 1 and 3
        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
            return False
    
        return True
        #a, b, c, d = s2
        #return s1 in (s2,  c+b+a+d, a+d+c+b, c+d+a+b)