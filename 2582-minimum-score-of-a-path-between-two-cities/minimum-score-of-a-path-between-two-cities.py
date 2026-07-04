class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))

        q = deque([1])
        seen = set({1})
        res = 'inf'

        while q:
            node = q.popleft()
            for nei, w in adj[node]:
                res = min(res, w)
                if nei in seen:
                    continue
                seen.add(nei)
                q.append(nei)
        
        return res