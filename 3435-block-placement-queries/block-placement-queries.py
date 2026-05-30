from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def kth(self, k):
        pos = 0
        bitmask = 1 << (self.n.bit_length() - 1)

        while bitmask:
            nxt = pos + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                pos = nxt
            bitmask >>= 1

        return pos + 1  # 1-based index


class SegTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * (4 * n)

    def update(self, idx, val, node, l, r):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)

        self.seg[node] = max(self.seg[node * 2], self.seg[node * 2 + 1])

    def query(self, ql, qr, node, l, r):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2
        return max(
            self.query(ql, qr, node * 2, l, mid),
            self.query(ql, qr, node * 2 + 1, mid + 1, r),
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = max(q[1] for q in queries)
        N = MAX_X + 1

        bit = Fenwick(N + 1)          # positions 0..MAX_X mapped to 1..N
        seg = SegTree(N)

        # obstacle at 0
        bit.add(1, 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                rank = bit.sum(x + 1)  # obstacles <= x
                prev_pos = bit.kth(rank) - 1

                total = bit.sum(N + 1)
                succ_pos = None
                if rank < total:
                    succ_pos = bit.kth(rank + 1) - 1

                if succ_pos is not None:
                    seg.update(
                        succ_pos,
                        succ_pos - x,
                        1,
                        0,
                        N - 1,
                    )

                seg.update(
                    x,
                    x - prev_pos,
                    1,
                    0,
                    N - 1,
                )

                bit.add(x + 1, 1)

            else:
                x, sz = q[1], q[2]

                rank = bit.sum(x + 1)
                prev_pos = bit.kth(rank) - 1

                best_gap = seg.query(0, x, 1, 0, N - 1)
                best_gap = max(best_gap, x - prev_pos)

                ans.append(best_gap >= sz)

        return ans