class Solution(object):
    def hasAllCodes(self, s, k):
        n = len(s)
        
        # Early impossibility check
        if n < k + 2**k - 1:
            return False

        codes = set()
        
        for i in range(n - k + 1):
            codes.add(s[i:i+k])
            if len(codes) == 2**k:
                return True
        
        return False
        
       
        