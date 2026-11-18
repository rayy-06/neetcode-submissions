class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a sliding window. left boundary l is fixed and r slides forward, consuming new characters
        # as r consumed characters, it adds them to a seen set
        # when r hits a character already in seen (duplicate), push l forward until l hits that duplicated char. once l is past there, the window can restart

        if len(s) == 0: return 0
        if len(s) == 1: return 1
        seen = set()
        l = 0
        r = 1
        seen.add(s[l])
        longest = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1

            else:
                # we hit a duplicate. save current size first
                longest = max(longest, r - l)    
                #dont include where r is right now, since thats the duplicated char
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        longest = max(longest, r - l)
        return longest










