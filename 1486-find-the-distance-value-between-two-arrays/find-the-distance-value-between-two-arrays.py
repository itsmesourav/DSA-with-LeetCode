class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n, m = len(arr1), len(arr2)
        res = 0

        for i in range(n):
            found = False
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    found = True
                    break
            if not found:
                res += 1
        return res