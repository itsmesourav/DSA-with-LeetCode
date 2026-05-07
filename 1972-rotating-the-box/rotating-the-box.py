class Solution(object):
    def rotateTheBox(self, boxGrid):
        n, m = len(boxGrid), len(boxGrid[0])

        for i in range(n):
            empty = m - 1
            for j in range(m - 1, -1, -1):
                val = boxGrid[i][j]
                if val == '*':
                    empty = j - 1
                elif val == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1
        
        res = [[None] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][n - 1 - i] = boxGrid[i][j]
        return res