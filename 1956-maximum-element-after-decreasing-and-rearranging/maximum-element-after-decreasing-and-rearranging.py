class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        n = len(arr)
        if arr[0] != 1:
            arr[0] = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                arr[i] = arr[i - 1] + 1
        
        return arr[-1]