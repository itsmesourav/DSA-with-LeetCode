class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        LOG = n.bit_length()

        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = parent[k][u]
                diff >>= 1
                k += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        masks = [1 << (ord(c) - ord('a')) for c in chars]

        for u in range(n):
            add(tin[u], masks[u])
            if tout[u] < n:
                add(tout[u], masks[u])

        def root_mask(u):
            return prefix(tin[u])

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))

                if masks[u] != new_mask:
                    delta = masks[u] ^ new_mask
                    add(tin[u], delta)
                    if tout[u] < n:
                        add(tout[u], delta)

                    masks[u] = new_mask
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)
                path_mask = root_mask(u) ^ root_mask(v) ^ masks[w]

                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer