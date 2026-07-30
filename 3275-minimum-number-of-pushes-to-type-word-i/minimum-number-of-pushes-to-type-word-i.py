class Solution(object):
    def minimumPushes(self, word):
        res = 0

        for i in range(len(word)):
            res += (i // 8) + 1

        return res