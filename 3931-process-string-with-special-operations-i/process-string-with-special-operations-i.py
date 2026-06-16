class Solution(object):
    def processStr(self, s):
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
        