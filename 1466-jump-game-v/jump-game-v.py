class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            res = 1

            # Right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))

            # Left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))

            memo[i] = res
            return res

        res = 1

        for i in range(n):
            res = max(res, dfs(i))

        return res