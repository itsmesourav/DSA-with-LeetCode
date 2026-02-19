class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1

            else:
                groups.append(count)
                count = 1
        groups.append(count)

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        
        return ans