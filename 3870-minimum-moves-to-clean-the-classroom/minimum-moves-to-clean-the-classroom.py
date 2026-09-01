from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        sr = sc = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)
        target = (1 << k) - 1

        q = deque([(sr, sc, energy, 0)])
        best = {(sr, sc, 0): energy}
        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == target:
                    return moves

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X' or e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    if best.get(key, -1) >= ne:
                        continue

                    best[key] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1