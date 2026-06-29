class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0

        for p in patterns:
            m = len(p)
            for i in range(len(word) - m + 1):
                j = 0
                while j < m and word[i + j] == p[j]:
                    j += 1
                if j == m:
                    res += 1
                    break
        
        return res