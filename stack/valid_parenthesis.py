class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif c == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif c == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c) # tricky: catch orphan right parenthesis

        return not stack  # unmatched left inside
