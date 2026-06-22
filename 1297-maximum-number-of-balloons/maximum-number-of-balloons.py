class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        fm = defaultdict(int)

        for c in text:
            if c in 'balloon':
                fm[c] += 1

        return min(fm['b'], fm['a'], fm['l'] // 2, fm['o'] // 2, fm['n'])