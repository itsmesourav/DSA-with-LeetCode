class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0

        mx = [nums[0]] * n
        pgcd = [nums[0]] * n

        for i in range(1, n):
            mx[i] = max(mx[i - 1], nums[i])
            pgcd[i] = self.gcd(nums[i], mx[i])

        pgcd.sort()

        res = 0
        for i in range(n // 2):
            res += self.gcd(pgcd[i], pgcd[n - 1 - i])

        return res