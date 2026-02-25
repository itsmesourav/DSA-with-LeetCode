class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = n * 5 // 100
        n = len(arr)
        arr.sort()
        x = arr[k: n - k]
        return sum(x) / len(x)
        