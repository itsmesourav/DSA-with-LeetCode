from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = SortedList(range(k))
        busy = []
        cnt = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, s = heapq.heappop(busy)
                free.add(s)

            if not free:
                continue

            j = free.bisect_left(i % k)

            if j == len(free):
                j = 0

            s = free.pop(j)
            cnt[s] += 1

            heapq.heappush(busy, (arrival[i] + load[i], s))

        mx = max(cnt)
        return [i for i in range(k) if cnt[i] == mx]