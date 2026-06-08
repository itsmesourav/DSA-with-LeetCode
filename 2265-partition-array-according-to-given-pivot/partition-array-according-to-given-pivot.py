class Solution(object):
    def pivotArray(self, nums, pivot):
        before = []
        mid = []
        after = []

        for n in nums:
            if n < pivot:
                before.append(n)
            elif n > pivot:
                after.append(n)
            else:
                mid.append(n)
        
        return before + mid + after