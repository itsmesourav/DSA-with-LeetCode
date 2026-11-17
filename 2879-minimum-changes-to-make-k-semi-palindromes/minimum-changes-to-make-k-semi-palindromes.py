class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                # Try every proper divisor of length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Compare mirrored characters in each group
                    for r in range(d):
                        left = r
                        right = ((length - 1 - r) // d) * d + r

                        while left < right:
                            if s[i + left] != s[i + right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # dp[p][i] = minimum changes to divide
        # first i characters into p substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    if cost[j][i - 1] != INF:
                        dp[p][i] = min(
                            dp[p][i],
                            dp[p - 1][j] + cost[j][i - 1]
                        )

        return dp[k][n]