class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x1, r1y1, r1x2, r1y2 = rec1
        r2x1, r2y1, r2x2, r2y2 = rec2

        return (
            max(r1x1, r2x1) < min(r1x2, r2x2) and
            max(r1y1, r2y1) < min(r1y2, r2y2)
        )