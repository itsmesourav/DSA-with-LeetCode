class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)

        #intervals.sort(key = lambda x: x[1])
        #intervals.sort(key = lambda x: x[0],  reverse = True)

        intervals.sort(key = lambda x: 
        (-x[0], x[1]))
        res = [intervals[0]]

        for i in range(1, n):
            while res and res[-1][0] >= intervals[i][0] and res[-1][1] <= intervals[i][1]:
                res.pop()
            res.append(intervals[i])
        
        return len(res)

        