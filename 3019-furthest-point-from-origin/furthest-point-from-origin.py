class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        l, r, res = 0, 0, 0

        for m in moves:
            if m == 'L':
                l += 1
            elif m == 'R':
                r += 1
            else:
                res += 1

        return res + abs(l - r)        