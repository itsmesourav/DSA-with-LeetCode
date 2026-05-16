class Solution(object):
    def findMin(self, nums):
        l = 0
        h = len(nums) - 1

        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] > nums[l]:
                h = mid
            else:
                h -= 1

        return nums[l]