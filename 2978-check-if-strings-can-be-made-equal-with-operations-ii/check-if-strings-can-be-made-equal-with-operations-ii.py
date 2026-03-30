class Solution(object):
    def checkStrings(self, s1, s2):
        n = len(s1)
        e1, o1 = defaultdict(int), defaultdict(int)
        e2, o2 = defaultdict(int), defaultdict(int)

        for i in range(n):
            if i % 2 == 0:
                e1[s1[i]] += 1
                e2[s2[i]] += 1
            else:
                o1[s1[i]] += 1
                o2[s2[i]] += 1
        return e1 == e2 and o1 == o2
        