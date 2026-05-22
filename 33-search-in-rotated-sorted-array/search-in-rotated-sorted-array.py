class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        start = l 
        l, r = 0, n - 1

        while l <= r:
            mid = l + (r - l) // 2
            realmid = (mid + start) % n
            if nums[realmid] > target :
                r = mid - 1
            elif nums[realmid] < target:
                l = mid + 1
            else:
                return realmid
            
        return - 1