class Solution:
    def isValid(self, s: str) -> bool:
        # map the openers to the closers
        ref = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        stack = []
        for char in s:
            if stack != [] and char in list(ref.values()) and stack[-1] in list(ref.keys()) and ref[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        return stack == []
        