class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        arr = []
        s = []
        for i in range(n): arr.append([i, positions[i], healths[i], directions[i]])
        arr.sort(key = lambda x: x[1])

        for i in range(n):
            idx, p, h, d = arr[i]
            if d == 'R': s.append([idx, p, h, d])
            else:
                while s and s[-1][3] == 'R':
                    if s[-1][2] == h:
                        s.pop()
                        h = 0
                        break
                    elif s[-1][2] > h:
                        s[-1][2] -= 1
                        h = 0
                        break
                    else:
                        s.pop()
                        h -= 1
                if h: s.append([idx, p, h, d])
        s.sort(key = lambda x: x[0])
        res = []
        for idx, p, h, d in s: res.append(h)
        return res