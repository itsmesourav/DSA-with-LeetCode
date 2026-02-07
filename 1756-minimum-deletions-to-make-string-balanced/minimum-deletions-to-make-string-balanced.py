class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        bCount = 0

        for i in s:
            if i == "b":
                bCount += 1
            else:
                res = min(res + 1, bCount)
        return res

        