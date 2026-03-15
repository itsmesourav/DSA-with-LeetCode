MOD = 10**9 + 7
class Fancy:

    def __init__(self):
        self.arr = []
        self.add = 0
        self.mul = 1
        

    def append(self, val: int) -> None:
        base = ((val - self.add) * pow(self.mul, -1, MOD)) % MOD
        self.arr.append(base)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % MOD
        













# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)