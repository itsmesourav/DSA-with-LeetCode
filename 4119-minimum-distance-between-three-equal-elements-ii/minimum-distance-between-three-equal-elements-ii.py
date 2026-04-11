class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        for i, n in enumerate(nums):
            mp[n].append(i)
        res = inf
        for n in mp:
            arr = mp[n]
            for i in range(len(arr) - 2):
                a, b, c = arr[i], arr[i + 1], arr[i + 2]
                res = min(res, abs(a - b) + abs(b - c) + abs(a - c))
        return res if res != inf else -1 