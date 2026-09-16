class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "{" : "}",
            "(": ")",
            "[" : "]"
        }

        stack = []

        for char in s:
            # if it is a key, push it
            if char in char_map:
                stack.append(char)

            # if not a key, is it the value to the key at the top? if not return false right here
            # if it is, pop it off

            elif stack != [] and char == char_map[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return stack == []


        
        


        
        