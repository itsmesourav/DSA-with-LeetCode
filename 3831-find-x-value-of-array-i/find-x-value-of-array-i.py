from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            value = num % k

            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[value] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * value) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add all subarrays ending at current position
            for r in range(k):
                result[r] += dp[r]

        return result