class Solution:

    def coord(self, char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
   
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 26

    
    def minWindow(self, s: str, t: str) -> str:
        map_t = [0] * 52
        map_s = [0] * 52
        num_found = 0
        result = ""

        if len(t) > len(s):
            return result
        
        my_set = set()
        for char in t:
            map_t[self.coord(char)] += 1
            my_set.add(char)
        needed = len(my_set)
        
        l = 0
        r = 0

        while r < len(s):
            if s[r] in t:
                map_s[self.coord(s[r])] += 1
                if map_s[self.coord(s[r])] == map_t[self.coord(s[r])]:
                    num_found += 1
                
            
            while num_found == needed:
                if s[l] in t:
                    map_s[self.coord(s[l])] -= 1
                    if map_s[self.coord(s[l])] < map_t[self.coord(s[l])]:
                        num_found -= 1
                    if num_found != needed:
                        cand = s[l: r+1]
                        if (result != "" and len(result) > len(cand)) or result == "":
                            result = cand    
                l += 1

            r += 1
        
        return result



                


        