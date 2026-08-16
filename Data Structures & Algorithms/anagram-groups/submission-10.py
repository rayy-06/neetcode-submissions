class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        # build char frequency tuple (slots 0 to 25 for a-z) and at the same time assign that as a key inside map

        for sub in strs:
            chars = [0] * 26
            for char in sub:
                chars[ord(char) - ord('a')] += 1
            
            chars_key = tuple(chars)
            if chars_key in map:
                map[chars_key].append(sub)
            else:
                map[chars_key] = [sub]
        
        return list(map.values())

        