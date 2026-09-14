class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # maintain a window of size: len(s1) and scan this window over s2
        # if the window has a frequency map matching s1, return true
        # shift the window over by one char at a time

        # O(1) space means we track the counts without an extra dynamic object, so use a fixed char array
        if len(s2) < len(s1):
            return False
        s1_map = [0]*26
        for char in s1:
            ind = ord(char) - ord('a')
            s1_map[ind] += 1
        
        s2_map = [0]*26

        for i in range(len(s1)):
            s2_map[
                ord(s2[i]) - ord('a')
            ] += 1
        if s2_map == s1_map:
            return True

        for l in range(1, len(s2) - len(s1) + 1):
            prev = ord(s2[l-1]) - ord('a')
            new = ord(s2[l + len(s1) - 1]) - ord('a')
            s2_map[prev] -=1
            s2_map[new] += 1
            if s1_map == s2_map:
                return True

        return False

        