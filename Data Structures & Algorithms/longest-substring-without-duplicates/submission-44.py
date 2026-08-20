class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        r = 0
        seen = set()
        size = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
                
     
            else:
 
             
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        return longest
            
            
        