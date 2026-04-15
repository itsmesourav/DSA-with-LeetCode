class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        res = float('inf')

        for i in range(n):
            if words[i] == target:
                d = abs(i -  startIndex)
                res = min(res, d, n - d)

        return res if res != float('inf') else -1
        