class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        c = '123456789'
        res = []

        for i in range(9):
            for j in range(i, 9):
                curr = c[i: j + 1]
                num = int(curr)
                if low <= num <= high:
                    res.append(num)
        
        res.sort()
        return res