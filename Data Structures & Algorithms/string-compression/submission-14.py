class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        l = 0
        r = 0
        while r <= len(chars):
            if r == len(chars) or chars[r] != chars[l]:
                last_window = r - l
                if last_window == 1:
                    res.append(chars[l])
                else:
                    res.append(f"{chars[l]}{last_window}")
                l = r
                if r == len(chars):
                    break

            else:
                r += 1

        res_string = "".join(res)
        print(res_string)
        for i in range(len(res_string)):
            chars[i] = res_string[i]
        return len(res_string)

        