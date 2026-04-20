class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        d1,  d2=  0, 0

        l, r = 0, n - 1
        while l < r:
            if colors[l] != colors[r]:
                d1 = r - l
                break
            else:
                l += 1
        l, r = 0, n - 1
        while l < r:
            if colors[l] != colors[r]:
                d2 = r - l
                break
            else:
                r -= 1
        return max(d1, d2)