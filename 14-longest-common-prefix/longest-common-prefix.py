class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while word[0:len(prefix)] != prefix:
                prefix = prefix[0:-1]

                if prefix == "":
                    return ""
        return prefix