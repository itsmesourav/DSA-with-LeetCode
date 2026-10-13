from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted((x * x for x in nums), reverse=True)
        half = (len(squares) + 1) // 2

        return sum(squares[:half]) - sum(squares[half:])