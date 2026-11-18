class Solution:
    def isValid(self, s: str) -> bool:
        # map the openers to the closers
        ref = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        # if opener, always push it
        # if closer, early return false if it doesnt close the char on top of stack
        stack = []
        for char in s:
            if char in ref:
                stack.append(char)
            else: # a closer
                if stack == [] or ref[stack.pop()] != char:
                    return False
        return stack == []
        