class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        d = 0
        for i in range(n):
            if s[i] in '(*':
                d += 1
            else:
                d -= 1
            if d < 0:
                return False

        d = 0    
        for i in range(n - 1, -1, -1):
            if s[i] in ')*':
                d += 1
            else:
                d -= 1
            if d < 0:
                return False
            
        return True