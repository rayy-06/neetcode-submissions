from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = defaultdict(int)
        max_count = 0
        best_length = 0
        l = 0

        for r in range(len(s)):
            ch = s[r]
            counts[ch] += 1
            max_count = max(max_count, counts[ch])

            window_length = r - l + 1

            # is this a valid window?
            # is this window length, minus most freq, below k? then,
            # this is a window where replacing all non freq is possible, 
            # using up to k replacements
            if (window_length - max_count) <= k:
                best_length = max(window_length, best_length)
            else: 
                # move l over since we dont have a valid window no more
                left_ch = s[l]
                counts[left_ch] -= 1
                l += 1
            
        return best_length





        