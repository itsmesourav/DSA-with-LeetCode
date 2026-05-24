class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def dfs(i):
            res = 1

            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dfs(j) + 1)

            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dfs(j) + 1)
            
            return res

        res = 1
        for i in range(n):
            res = max(res, dfs(i))
        return res