class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [-1] * n
        order = []
        timer = 0

        # Iterative DFS and Euler tour
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                order.append(u)
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting for LCA
        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        for u in range(n):
            up[0][u] = u if parent[u] == -1 else parent[u]

        for k in range(1, LOG):
            for u in range(n):
                up[k][u] = up[k - 1][up[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return up[0][u]

        # Fenwick tree with XOR masks
        bit = [0] * (n + 1)

        def add(i, mask):
            i += 1
            while i <= n:
                bit[i] ^= mask
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_xor(left, right):
            if left > right:
                return 0
            result = prefix(right)
            if left > 0:
                result ^= prefix(left - 1)
            return result

        masks = [1 << (ord(c) - ord('a')) for c in chars]

        # Each node contributes its character over its subtree interval.
        for u in range(n):
            add(tin[u], masks[u])
            if tout[u] < n:
                add(tout[u], masks[u])

        # Prefix XOR of active ancestors, using Euler difference events.
        # The second event cancels the contribution after the subtree.
        # Point prefix queries recover the root-to-node character mask.
        # Rebuild using standard difference-array Fenwick updates.
        bit = [0] * (n + 1)

        def update_event(i, mask):
            add(i, mask)

        for u in range(n):
            update_event(tin[u], masks[u])
            if tout[u] < n:
                update_event(tout[u], masks[u])

        def root_mask(u):
            return prefix(tin[u])

        answers = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))

                if masks[u] != new_mask:
                    delta = masks[u] ^ new_mask
                    update_event(tin[u], delta)
                    if tout[u] < n:
                        update_event(tout[u], delta)
                    masks[u] = new_mask
                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                path_mask = root_mask(u) ^ root_mask(v) ^ masks[w]

                # A palindrome permutation allows at most one odd frequency.
                answers.append((path_mask & (path_mask - 1)) == 0)

        return answers