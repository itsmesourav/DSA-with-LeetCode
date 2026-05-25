class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        dp = [False] * n
        dp[0] = True
        last = 0

        for i in range(n):
            if dp[i]:
                l = max(i + minJump, last + 1)
                h = min(i + maxJump, n - 1)
                if l <= h:
                    for j in range(l, h + 1):
                        if s[j] == '0':
                            dp[j] = True
                    last = h
        
        return dp[-1]