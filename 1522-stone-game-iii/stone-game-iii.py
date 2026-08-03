class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dp(i):
            if i >= n:
                return 0
            best = -inf
            score = 0
            for x in range(1, 4):
                if i + x > n:
                    break
                score += stoneValue[i  + x - 1]
                best = max(best, score - dp(i + x))
            return best
        
        n = len(stoneValue)
        balance = dp(0)
        if balance > 0:
            return 'Alice'
        if balance < 0:
            return 'Bob'
        return 'Tie'