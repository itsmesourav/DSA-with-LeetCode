from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # Step 0: Basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        # DSU (Union-Find)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Step 1: Union indices where lcp[i][j] > 0
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        # Step 2: Assign smallest characters
        char_map = {}
        res = [''] * n
        current_char = ord('a')
        
        for i in range(n):
            root = find(i)
            if root not in char_map:
                if current_char > ord('z'):
                    return ""  # more than 26 groups
                char_map[root] = chr(current_char)
                current_char += 1
            res[i] = char_map[root]
        
        word = "".join(res)
        
        # Step 3: Validate LCP
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 0
                
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word