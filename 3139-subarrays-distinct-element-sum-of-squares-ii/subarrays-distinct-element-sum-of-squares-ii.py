
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        size = 4 * n
        total = [0] * size
        squares = [0] * size
        lazy = [0] * size

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                length = right - left + 1
                squares[node] = (
                    squares[node] + 2 * lazy[node] * total[node]
                    + lazy[node] * lazy[node] * length
                ) % MOD
                total[node] = (total[node] + lazy[node] * length) % MOD
                lazy[node] = (lazy[node] + 1) % MOD
                return

            mid = (left + right) // 2
            lc = node * 2
            rc = lc + 1

            if ql <= mid:
                update(lc, left, mid, ql, qr)
            if qr > mid:
                update(rc, mid + 1, right, ql, qr)

            total[node] = (total[lc] + total[rc]) % MOD
            squares[node] = (squares[lc] + squares[rc]) % MOD

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            for child, l, r in (
                (node * 2, left, mid),
                (node * 2 + 1, mid + 1, right)
            ):
                length = r - l + 1
                add = lazy[node]
                squares[child] = (
                    squares[child] + 2 * add * total[child]
                    + add * add * length
                ) % MOD
                total[child] = (total[child] + add * length) % MOD
                lazy[child] = (lazy[child] + add) % MOD

            lazy[node] = 0

        # Rebuild the update function with lazy propagation.
        def add_range(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                length = right - left + 1
                add = 1
                squares[node] = (
                    squares[node] + 2 * add * total[node]
                    + add * add * length
                ) % MOD
                total[node] = (total[node] + add * length) % MOD
                lazy[node] = (lazy[node] + add) % MOD
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                add_range(node * 2, left, mid, ql, qr)
            if qr > mid:
                add_range(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        ans = 0
        last = {}

        for i, x in enumerate(nums):
            start = last.get(x, -1) + 1
            add_range(1, 0, n - 1, start, i)
            ans = (ans + squares[1]) % MOD
            last[x] = i

        return ans
