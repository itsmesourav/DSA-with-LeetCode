class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        mp = defaultdict(list)

        for r, c in reservedSeats:
            mp[r - 1].append(c - 1)

        res = 0
        seenr = 0

        for k in mp:
            seenr += 1

            left = all(c not in mp[k] for c in range(1, 5))
            middle = all(c not in mp[k] for c in range(3, 7))
            right = all(c not in mp[k] for c in range(5, 9))

            res += max(middle, left + right)

        return res + (n - seenr) * 2