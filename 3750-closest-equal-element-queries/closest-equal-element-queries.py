class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)

        res = []
        for q in queries:
            t = nums[q]
            arr = mp[t]
            s = len(arr)
            if s <= 1:
                res.append(-1)
            elif s == 2:
                d = abs(arr[0] - arr[1])
                res.append(min(d, n - d))
            else:
                i = bisect.bisect_left(arr, q)
                prev = arr[(i - 1) % s]
                next = arr[(i + 1) % s]

                curr = 'inf'
                d1 = abs(prev - arr[i])
                curr = min(curr, d1, n - d1)
                d2 =  abs(next - arr[i])
                curr = min(curr, d2, n - d2)

                res.append(curr)
        return res