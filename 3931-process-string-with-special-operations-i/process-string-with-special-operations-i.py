class Solution:
    def processStr(self, s: str) -> str:
        arr = []

        for c in s:
            if c.islower():
                arr.append(c)
            elif arr and c == '*':
                arr.pop()
            elif c == '#':
                arr += arr
            elif c == '%':
                arr = arr[::-1]
        
        return "".join(arr)