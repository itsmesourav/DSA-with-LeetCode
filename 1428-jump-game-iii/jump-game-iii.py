class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        def dfs(i):
            if i < 0 or i >= n or i in seen:
                return False
            if arr[i] == 0:
                return True
            seen.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])
        
        seen = set()
        n = len(arr)
        return dfs(start)
        