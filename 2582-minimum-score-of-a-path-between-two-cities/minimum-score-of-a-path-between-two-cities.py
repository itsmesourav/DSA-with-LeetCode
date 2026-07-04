class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))

        q = deque([1])
        seen = set({1})
        res = inf

        while q:
            node = q.popleft()
            for nei, w in adj[node]:
                res = min(res, w)
                if nei in seen:
                    continue
                seen.add(nei)
                q.append(nei)
        
        return res