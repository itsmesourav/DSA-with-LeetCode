class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)

        for i in range(n):
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False
        