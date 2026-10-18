class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations C(n, r)
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] +
                              comb[i - 1][j]) % MOD

        def countWays(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = countWays(left)
            right_ways = countWays(right)

            total = len(left) + len(right)

            return (comb[total][len(left)] *
                    left_ways % MOD * right_ways) % MOD

        return (countWays(nums) - 1) % MOD