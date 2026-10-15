class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        define a set covered
        sl

        greedily create new substrings with the constraint:
        if a letter is already in one substring, it cannot appear in another one

        at a given character we can choose to 1:
        continue the last substring or
        start a new one, ending the last one

        if the same char we are at exists later, we MUST continue the current substring

        if the char we are at does not exist later, it is optimal to start a new one

        how do we know if char exists or doesnt? keep a hashmap as we traverse. 
        update as we go. delete entries as they get used up

        keep track of the chars we have encountered in the current substring. 
        we cannot end it until all are exhasusted

        ex. start at x. now we keep going until no x left
        next, we hit a y. keep going till no y left. that is why the first substring is xyxxy

        so as we traverse we need to keep track of 
        1. state of entire string, updated based on what is remaining as chars are consumed
        2. state of the distinct num of chars we have consumed so far

        """
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 1
            else:
                freq_map[char] += 1
        
        l = 0
        r = 0
        
        in_sub = set()
        res = []

        while r < len(s):
            if s[r] not in in_sub:
                in_sub.add(s[r])
            freq_map[s[r]] -= 1

            # check if all chars in_sub are now removed from freq_map (or have 0 freq)
            complete = True
            for char in in_sub:
                if freq_map[char] > 0:
                    complete = False
            
            if complete:
                res.append(r-l + 1)
                in_sub.clear()
                l = r + 1
            r += 1
        return res





















        