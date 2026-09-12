import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        intervalsi = {}

        for i, (l, r, w) in enumerate(intervals):
            if (l, r, w) not in intervalsi:
                intervalsi[(l, r, w)] = i

        intervals = sorted(intervalsi)
        n = len(intervals)

        memo = {}

        def dp(i, rem):
            if rem == 0 or i == n:
                return 0, []

            if (i, rem) in memo:
                return memo[(i, rem)]

            # Skip
            skipw, skip_indices = dp(i + 1, rem)

            # Take
            l, r, w = intervals[i]

            nexti = bisect.bisect_left(intervals, (r + 1,))

            nextw, next_indices = dp(nexti, rem - 1)

            takew = w + nextw
            take_indices = next_indices + [intervalsi[intervals[i]]]
            take_indices.sort()

            if takew > skipw:
                ans = (takew, take_indices)

            elif takew < skipw:
                ans = (skipw, skip_indices)

            else:
                if take_indices < skip_indices:
                    ans = (takew, take_indices)
                else:
                    ans = (skipw, skip_indices)

            memo[(i, rem)] = ans
            return ans

        return dp(0, 4)[1]