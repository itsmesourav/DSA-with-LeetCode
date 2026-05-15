class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        res = 0
        avail = 0

        for c, t in tasks:
            need = t - avail
            if need > 0:
                res += need
                avail += need
            avail -= c
        return res
        