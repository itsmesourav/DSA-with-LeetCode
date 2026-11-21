from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        # Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Find new parents using DFS
        new_parent = parent[:]
        last = [-1] * 26

        stack = [(0, False, -1)]

        while stack:
            node, exiting, old = stack.pop()
            ch = ord(s[node]) - ord('a')

            if not exiting:
                previous = last[ch]

                if previous != -1:
                    new_parent[node] = previous

                last[ch] = node

                stack.append((node, True, previous))

                for child in reversed(children[node]):
                    stack.append((child, False, -1))

            else:
                last[ch] = old

        # Build final tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        ans = [1] * n
        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        for node in reversed(order):
            if new_parent[node] != -1:
                ans[new_parent[node]] += ans[node]

        return ans