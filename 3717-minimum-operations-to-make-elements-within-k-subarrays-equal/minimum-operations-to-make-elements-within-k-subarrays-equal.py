
from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(i, c, s):
            i += 1
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def query(tree, i):
            res = 0
            while i > 0:
                res += tree[i]
                i -= i & -i
            return res

        def kth(kth_pos):
            idx = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= m and cnt[nxt] < kth_pos:
                    kth_pos -= cnt[nxt]
                    idx = nxt
                bit >>= 1

            return idx

        # Calculate the cost of every window.
        costs = []
        total = 0

        for i, v in enumerate(nums):
            p = bisect_left(vals, v)
            update(p, 1, v)
            total += v

            if i >= x:
                old = nums[i - x]
                q = bisect_left(vals, old)
                update(q, -1, -old)
                total -= old

            if i >= x - 1:
                mid_idx = kth((x + 1) // 2)
                mid = vals[mid_idx]

                lc = query(cnt, mid_idx)
                ls = query(sm, mid_idx)

                rc = query(cnt, m) - query(cnt, mid_idx + 1)
                rs = query(sm, m) - query(sm, mid_idx + 1)

                cost = mid * lc - ls + rs - mid * rc
                costs.append(cost)

        # DP with rolling arrays.
        inf = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            cur = [inf] * (n + 1)

            for i in range(1, n + 1):
                cur[i] = cur[i - 1]

                if i >= x and prev[i - x] != inf:
                    cur[i] = min(
                        cur[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = cur

        return prev[n]
