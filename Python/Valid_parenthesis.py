class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            symbols = ['(', '{', '[']
            if i in symbols:
                stack.append(i)
            elif i == ')' and len(stack)!=0 and stack[-1] == '(' :
                stack.pop()
            elif i =='}' and len(stack)!=0 and stack[-1] == '{':
                stack.pop()
            elif i == ']' and len(stack)!=0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return stack == []