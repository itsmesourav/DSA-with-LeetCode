class Solution(object):
    def runningSum(self, nums):

        total = 0
        result = []
        for num in nums:
            total += num
            result.append(total)
        return result
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        