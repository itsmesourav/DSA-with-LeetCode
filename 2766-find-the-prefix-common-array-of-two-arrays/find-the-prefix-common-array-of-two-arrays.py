class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        sa = set()
        sb = set()
        both = set()
        res = []

        for i in range(n):
            sa.add(A[i])
            sb.add(B[i])
            if A[i] in sb:
                both.add(A[i])
            if B[i] in sa:
                both.add(B[i])
            res.append(len(both))
        return res