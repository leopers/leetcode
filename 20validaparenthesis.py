class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if(len(stack)!= 0): print(stack[-1])
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif not stack:
                return False
            elif (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                return False

        return len(stack) == 0