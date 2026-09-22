from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [(1, [0] * k) for _ in range(2 * size)]

        def make(x):
            x %= k
            cnt = [0] * k
            cnt[x] = 1
            return x, cnt

        def merge(a, b):
            p1, c1 = a
            p2, c2 = b

            cnt = c1[:]

            for r in range(k):
                cnt[(p1 * r) % k] += c2[r]

            return (p1 * p2) % k, cnt

        for i in range(n):
            tree[size + i] = make(nums[i])

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(index, value):
            p = size + index
            tree[p] = make(value)

            p //= 2
            while p:
                tree[p] = merge(tree[p * 2], tree[p * 2 + 1])
                p //= 2

        def query(left):
            l = left + size
            r = n + size

            left_part = (1, [0] * k)
            right_part = (1, [0] * k)

            while l < r:
                if l & 1:
                    left_part = merge(left_part, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right_part = merge(tree[r], right_part)

                l //= 2
                r //= 2

            return merge(left_part, right_part)

        ans = []

        for index, value, start, x in queries:
            update(index, value)

            _, cnt = query(start)
            ans.append(cnt[x])

        return ans