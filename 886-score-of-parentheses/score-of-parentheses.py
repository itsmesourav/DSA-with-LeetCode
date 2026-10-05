class Solution(object):
    def scoreOfParentheses(self, s):
        d = 0
        prev = ''
        res = 0

        for c in s:
            if c == '(':
                d += 1
            else:
                d -= 1
            if prev == '(' and c == ')':
                res += 1 << d
            prev = c
        
        return res