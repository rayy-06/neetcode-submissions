class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            char_map = [0] * 26
            for char in s:
                char_map[ord(char) - ord('a')] += 1
            k = tuple(char_map)
            if k not in result:
                result[k] = [s]
            else:
                result[k].append(s)
        return list(result.values())
        