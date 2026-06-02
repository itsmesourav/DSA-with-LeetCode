class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        res = inf

        for i in range(n):
            for j in range(m):
                ls, ld =  landStartTime[i], landDuration[i]
                ws, wd = waterStartTime[j], waterDuration[j]

                if ls <= ws:
                    res = min(res, max(ls + ld, ws) + wd)
                else:
                    res = min(res, max(ws + wd, ls) + ld)

        return res