class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if not self.par[x] == x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.par[pa] = pb
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UF(n)

        for a, b in allowedSwaps:
            uf.union(a, b)
        
        groups = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            groups[uf.find(i)][source[i]] += 1
        
        res = 0
        for i in range(n):
            g = groups[uf.find(i)]
            t = target[i]
            if g[t] > 0:
                g[t] -= 1
            else:
                res += 1
        
        return res
        