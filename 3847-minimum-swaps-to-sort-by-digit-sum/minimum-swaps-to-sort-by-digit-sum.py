class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        index_map = {num: i for i, num in enumerate(nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or index_map[sorted_nums[i]] == i:
                visited[i] = True
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = index_map[sorted_nums[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps