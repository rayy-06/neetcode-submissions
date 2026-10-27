class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            prefix = f"{len(s)}#"
            new = prefix + s
            result += new
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            # now we hit the delimiter, so pull the length and read the right num of chars

            length_num = int(length)
            sub = s[i + 1: i + 1 + length_num]
            result.append(sub)
            i += length_num + 1
        return result

        

