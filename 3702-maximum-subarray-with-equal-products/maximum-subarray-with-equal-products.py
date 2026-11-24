
class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                product *= x
                g = gcd(g, x)
                l = (l * x) // gcd(l, x)

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans