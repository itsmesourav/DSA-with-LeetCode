from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        # value -> list of indices
        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        q = deque([0])
        visited = set([0])
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                # reached last index
                if i == n - 1:
                    return steps

                neighbors = []

                # same value jumps
                neighbors.extend(graph[arr[i]])

                # adjacent jumps
                if i + 1 < n:
                    neighbors.append(i + 1)

                if i - 1 >= 0:
                    neighbors.append(i - 1)

                for nei in neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

                # IMPORTANT:
                # avoid re-processing same value indices
                graph[arr[i]].clear()

            steps += 1

        return -1