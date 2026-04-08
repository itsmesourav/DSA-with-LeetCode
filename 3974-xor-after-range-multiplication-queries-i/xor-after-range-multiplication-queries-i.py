class Solution(object):
    def xorAfterQueries(self, nums, queries):
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k
        res = 0
        for x in nums:
            res ^= x
        return res
        