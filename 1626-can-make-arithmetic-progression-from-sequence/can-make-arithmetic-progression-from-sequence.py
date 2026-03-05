class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        a = arr[0]
        d = arr[1] - arr[0]
        ans = n*(2*a + (n - 1)*d)//2
        
        if sum(arr)!=ans:
            return False

        for i in range(2, n):
            if arr[i] - arr[i - 1]!=d:
                return False
        
        return True