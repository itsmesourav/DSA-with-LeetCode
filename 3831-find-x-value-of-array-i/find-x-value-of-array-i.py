class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        prev = [0] * k

        for num in nums:
            x = num % k
            cur = [0] * k

            # Start a new subarray
            cur[x] += 1

            # Extend previous subarrays
            for r in range(k):
                cur[(r * x) % k] += prev[r]

            # Add to answer
            for r in range(k):
                ans[r] += cur[r]

            prev = cur

        return ans