class Solution(object):
    def robotSim(self, commands, obstacles):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0
        res = 0
        obs = set()
        for a, b in obstacles:
            obs.add((a, b))
        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                for i in range(c):
                    nx, ny = x + dirs[d][0], y + dirs[d][1]
                    if (nx, ny) in obs:
                        break
                    res = max(res, nx**2 + ny**2)
                    x, y = nx, ny
        return res
        