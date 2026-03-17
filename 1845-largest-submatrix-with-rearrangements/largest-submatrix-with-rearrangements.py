class Solution(object):
    def largestSubmatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        acc = [0] * m
        res = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    acc[j] += 1
                else:
                    acc[j] =0

            s = sorted(acc, reverse = True)
            for ci in range(len(s)):
                res = max(res, s[ci] * (ci + 1))
        
        return res