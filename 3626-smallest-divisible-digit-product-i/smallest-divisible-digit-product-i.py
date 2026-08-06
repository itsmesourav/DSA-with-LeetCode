class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            p = 1
            curr = n
            while curr:
                p *= curr % 10
                curr //= 10
            
            if p % t == 0:
                return n
            n += 1