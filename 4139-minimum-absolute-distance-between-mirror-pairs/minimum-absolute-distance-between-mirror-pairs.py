class Solution(object):
    def minMirrorPairDistance(self, nums):
        rev = {}
        res = 'inf'

        for i, n in enumerate(nums):
            if n in rev:
                res = min(res, i - rev[n])
            r = int(str(n)[::-1])
            rev[r] = i
        
        return res if res != 'inf' else -1