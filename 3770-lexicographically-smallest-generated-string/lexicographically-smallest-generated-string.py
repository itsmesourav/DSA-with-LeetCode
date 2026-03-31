class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = ['?'] * (n + m - 1)
        locked = [False] * (n + m - 1)
        
        # Step 1: Apply 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] == '?' or res[i + j] == str2[j]:
                        res[i + j] = str2[j]
                        locked[i + j] = True
                    else:
                        return ""
        
        # Step 2: Fill remaining with 'a'
        for i in range(len(res)):
            if res[i] == '?':
                res[i] = 'a'
        
        # Step 3: Fix 'F'
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(res[i:i+m]) == str2:
                    fixed = False
                    
                    # RIGHT → LEFT (important)
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not locked[pos]:
                            original = res[pos]
                            
                            for ch in 'abcdefghijklmnopqrstuvwxyz':
                                if ch == original:
                                    continue
                                res[pos] = ch
                                
                                if ''.join(res[i:i+m]) != str2:
                                    fixed = True
                                    break
                            
                            if fixed:
                                break
                            res[pos] = original
                    
                    if not fixed:
                        return ""
        
        return ''.join(res)