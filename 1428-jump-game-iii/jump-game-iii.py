class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
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