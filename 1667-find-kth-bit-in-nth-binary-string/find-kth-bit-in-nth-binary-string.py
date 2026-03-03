class Solution:
    def findKthBit(self, n: int, k: int) -> str:
         return "0" if n == 1 else (
            "1" if k == 1 << (n - 1) else
            self.findKthBit(n - 1, k) if k < 1 << (n - 1) else
            str(1 - int(self.findKthBit(n - 1, (1 << n) - k)))
        )
        