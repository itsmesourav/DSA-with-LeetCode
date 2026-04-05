class Solution:
    def judgeCircle(self, moves: str) -> bool:
        fm = defaultdict(int)
        for m in moves:
            fm[m] += 1
        return fm['U'] == fm['D'] and fm['L'] == fm['R']       