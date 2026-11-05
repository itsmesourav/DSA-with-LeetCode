class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
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