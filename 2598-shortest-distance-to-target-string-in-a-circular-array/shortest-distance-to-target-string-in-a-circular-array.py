class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = inf

        for i in range(n):
            if words[i] == target:
                d = abs(i -  startIndex)
                res = min(res, d, n - d)

        return res if res != inf else -1