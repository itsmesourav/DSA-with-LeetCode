class Solution(object):
    def angleClock(self, hour, minutes):
        d1 = (hour * 30) + (0.5 * minutes)
        d2 = minutes * 6
        dif = abs(d1 - d2)
        return min(dif, 360 - dif)
        