class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def bt(curr):
            if len(curr) == n:
                res.append(curr)
                return

            for c in 'abc' :
                if not curr or curr[-1] != c:
                    bt(curr + c)

        bt('')
        if k > len(res):
            return ""

        return res[k - 1]
        
        