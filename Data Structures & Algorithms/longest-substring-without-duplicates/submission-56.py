class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        seen = set()

        if len(s) == 1:
            return 1   

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                cand = r - l + 1
                res = max(res, cand)
                r += 1
 
            else:
                # save the last window
                cand = (r-1) - l + 1
                res = max(res, cand)

                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[r])
                l += 1
        return res
                
        