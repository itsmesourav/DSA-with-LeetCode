class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
        self.components = n

    def findparent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findparent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ulp_u = self.findparent(u)
        ulp_v = self.findparent(v)
        if ulp_u == ulp_v:
            return False

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] + self.size[ulp_v]

        self.components -= 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can_achieve(S):
            dsu = DSU(n)
            upgrades = 0

            for u,v,s,must in edges:
                if must == 1:
                    if s < S:
                        return False
                    if not dsu.union(u,v):
                        return False
            
            for u,v,s,must in edges:
                if must == 0 and s >= S:
                    dsu.union(u,v)

            for u,v,s,must in edges:
                if must == 0 and s < S and 2*s >= S:
                    if dsu.findparent(u) != dsu.findparent(v):
                        if upgrades >= k:
                            return False
                        dsu.union(u,v)
                        upgrades += 1

            return dsu.components == 1

        left = 1
        right = 2*10**5
        ans =- 1

        while left <= right:
            mid = (left + right)//2
            if can_achieve(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        

        