class Solution(object):
    def findKthBit(self, n, k):
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)
        
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        return "1" if self.findKthBit(n - 1, 2 * mid - k) == "0" else "0"
        
        