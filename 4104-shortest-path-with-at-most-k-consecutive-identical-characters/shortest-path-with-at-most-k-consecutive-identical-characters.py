
import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        if k == 0:
            return -1

        adj = [[] for _ in range(n)]

        for a, b, wt in edges:
            adj[a].append((b, wt))

        pq = [(0, 0, 1)]
        visited = {}

        while pq:
            cost, node, streak = heapq.heappop(pq)

            state = (node, streak)

            if state in visited:
                continue

            visited[state] = cost

            if node == n - 1:
                return cost

            for nxt, wt in adj[node]:

                if labels[nxt] == labels[node]:
                    next_streak = streak + 1
                else:
                    next_streak = 1

                if next_streak <= k:
                    next_state = (nxt, next_streak)

                    if next_state not in visited:
                        heapq.heappush(
                            pq,
                            (cost + wt, nxt, next_streak)
                        )

        return -1
