class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        middle = []
        after = []

        for n in nums:
            if n > pivot:
                after.append(n)
            elif n < pivot:
                before.append(n)
            else:
                middle.append(n)
        
        return before + middle + after