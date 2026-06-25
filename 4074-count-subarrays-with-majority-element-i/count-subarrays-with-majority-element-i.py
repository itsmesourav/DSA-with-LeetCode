class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        res = 0

        for i in range(n):
            targetc = 0
            for j in range(i, n):
                if nums[j] == target:
                    targetc += 1
                if targetc > (j - i + 1) // 2:
                    res += 1
        
        return res