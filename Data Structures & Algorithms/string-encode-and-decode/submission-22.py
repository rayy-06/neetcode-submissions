class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}*")
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == "*":
                l = int(s[i:j])
                string = s[j + 1: j + 1 + l]
                res.append(string)
                i = j + 1 + l
                j = i
            else:
                j += 1
        return res

"""
idea: combine each string in the array into one string. each distinct string is seperated by a delimiter token (specify a new string) and a number (how many chars does the incoming string have)
looks like this

["hi", "hello"] <-----> "*2hi*5hello"
this works, even if *, or a digit could appear in a string. why? the digit consumes the exact number of chars needed without caring about the contents
"""
