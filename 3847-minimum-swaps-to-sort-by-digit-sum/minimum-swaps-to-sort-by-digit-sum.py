from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)
        ordered = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {value: i for i, value in enumerate(nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or position[ordered[i]] == i:
                visited[i] = True
                continue

            cycle_size = 0
            current = i

            while not visited[current]:
                visited[current] = True
                current = position[ordered[current]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps