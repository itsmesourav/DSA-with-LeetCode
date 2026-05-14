class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        
        n = nums[-1]
        
        # Length must be n + 1
        if len(nums) != n + 1:
            return False
        
        # Check 1 to n-1
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        
        # Last two elements must be n
        return nums[-1] == n and nums[-2] == n