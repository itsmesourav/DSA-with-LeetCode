
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Step 1: Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Find new parents using DFS
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

        # Step 3: Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        ans = [1] * n
        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        for node in reversed(order):
            if new_parent[node] != -1:
                ans[new_parent[node]] += ans[node]

        return ans