class Solution(object):
    def minOperations(self, nums):
        n = len(nums)

        # Check if nums is a rotation of the sorted array
        for i in range(n):
            if nums[i] != (nums[0] + i) % n:
                break
        else:
            k = nums.index(0)
            return min(k, n - k + 2) if k != 0 else 0

        # Check if reversing nums gives a rotation of the sorted array
        rev = nums[::-1]
        for i in range(n):
            if rev[i] != (rev[0] + i) % n:
                break
        else:
            k = rev.index(0)
            return min(k + 1, n - k + 1)

        return -1