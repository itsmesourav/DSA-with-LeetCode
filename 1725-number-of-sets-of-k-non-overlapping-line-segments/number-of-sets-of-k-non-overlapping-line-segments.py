class Solution(object):

    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        result = 1
        r = 2 * k
        total = n + k - 1

        for i in range(1, r + 1):
            result = result * (total - r + i) % MOD
            result = result * pow(i, MOD - 2, MOD) % MOD

        return result