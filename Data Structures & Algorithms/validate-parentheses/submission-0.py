class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        str = list(s)
        if len(str) % 2 != 0:
            return False
        else: pass

        for i in range(len(s)):
            if str[i] == "(" or str[i] == "[" or str[i] == "{":
                stack.append(str[i])
            elif str[i] == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif str[i] == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif str[i] == "}" and stack and stack[-1] == "{":
                stack.pop()
            else: return False
        return True if len(stack) == 0 else False