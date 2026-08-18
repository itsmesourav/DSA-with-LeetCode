class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        if k == n:
            return max(nums)
        
        fm = defaultdict(int)
        for num in nums:
            fm[num] += 1
        
        unique = []
        for num, v in fm.items():
            if v == 1:
                unique.append(num)
        
        if k == 1:
            return max(unique) if unique else -1
        first = nums[0] if fm[nums[0]] == 1 else -1
        last = nums[-1] if fm[nums[-1]] == 1 else -1
        return max(first, last)