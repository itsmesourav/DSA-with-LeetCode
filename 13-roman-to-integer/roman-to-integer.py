class Solution(object):
    def romanToInt(self, s):
        total = 0
        for i in range(len(s)):
            if s[i] == "I":
                value = 1
            elif s[i] == "V":
                value = 5
            elif s[i] == "X":
                value = 10
            elif s[i] == "L":
                value = 50
            elif s[i] == "C":
                value = 100
            elif s[i] == "D":
                value = 500
            else:
                value = 1000

            if i + 1 < len(s):
                if s[i+1] == "I":
                    next_val = 1
                elif s[i+1] == "V":
                    next_val = 5
                elif s[i+1] == "X":
                    next_val = 10
                elif s[i+1] =="L":
                    next_val = 50
                elif s[i+1] == "C":
                    next_val = 100
                elif s[i+1] == "D":
                    next_val = 500
                else:
                    next_val = 1000

                if value < next_val:
                    total -= value
                else:
                    total += value
            else:
                total += value
        return total
