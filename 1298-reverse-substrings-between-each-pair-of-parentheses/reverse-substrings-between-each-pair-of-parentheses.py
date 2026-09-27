class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for c in s:
            if c == ')':
                curr = []
                while stack and stack[-1] != '(':
                    curr.append(stack.pop())
                stack.pop()
                stack += curr
            else:
                stack.append(c)
        return "".join(stack)