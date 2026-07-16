class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = [nums[0]] * n
        pgcd = [nums[0]] * n

        for i in range(1, n):
            mx[i] = max(mx[i - 1], nums[i])
            pgcd[i] = gcd(nums[i], mx[i])

        pgcd.sort()

        res = 0
        for i in range(n // 2):
            res += gcd(pgcd[i], pgcd[n - 1 - i])

        return res