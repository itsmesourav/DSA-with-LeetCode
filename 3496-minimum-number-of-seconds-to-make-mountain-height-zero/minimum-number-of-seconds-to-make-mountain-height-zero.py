class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        h = []

        for x in workerTimes:
            heapq.heappush(h, (x, x, 2))

        for x in range(mountainHeight):
            acc, base, count = heapq.heappop(h)
            res = acc
            heapq.heappush(h, (acc + base * count, base, count + 1))

        return res
      