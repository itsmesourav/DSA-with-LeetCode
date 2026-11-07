import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        time = 0

        for i, t in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, w, idx = heapq.heappop(busy)
                    heapq.heappush(free, (w, idx))

            w, idx = heapq.heappop(free)
            ans.append(idx)

            heapq.heappush(busy, (time + t, w, idx))

        return ans