class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n, m = len(landStartTime), len(waterStartTime)

        res = 'inf'

        def check(s1, d1, s2, d2):
            f1 = 'inf'
            for i in range(len(s1)):
                f1 = min(f1, s1[i] + d1[i])
            
            f2 = 'inf'
            for i in range(len(s2)):
                f2 = min(f2, max(f1, s2[i]) + d2[i])
            return f2

        return min(
            check(landStartTime, landDuration, waterStartTime, waterDuration),
            check(waterStartTime, waterDuration, landStartTime, landDuration)
        )
        