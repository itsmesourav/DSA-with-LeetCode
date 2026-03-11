class Solution(object):
    def intersection(self, nums1, nums2):
        res = set()
        for i in nums1:
            if i in nums2:
                res.add(i)
        return list(res)