class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        dif = [0] * (2 * limit + 2)

        for i in range(n // 2):
            l = nums[i]
            r = nums[n - 1 - i]

            dif[min(l, r) + 1] -= 1
            dif[l + r] -= 1
            dif[l + r + 1] += 1
            dif[max(l, r) + limit + 1] += 1
        
        res, curr = n, n
        for i in range(2, 2 * limit + 1):
            curr += dif[i]
            res = min(res, curr)
        
        return res
        