class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        balance = 0

        for ch in s:
            if ch == '(':
                if balance > 0:
                    result.append(ch)
                balance += 1

            else:
                balance -= 1
                if balance > 0:
                    result.append(ch)

        return ''.join(result)