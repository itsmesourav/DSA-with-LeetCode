class Solution(object):
    def getCommon(self, nums1, nums2):
        res = 'inf'

        nums1 = set(nums1)
        nums2 = set(nums2)

        for x in nums1:
            if x in nums2:
                res = min(res, x)

        return res if res != 'inf' else -1        