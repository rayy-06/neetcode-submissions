class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # define the answer space
        m = 0
        s = 0
        for w in weights:       # find max and sum in one pass
            m = max(m, w)
            s += w
        
        l = m
        r = s

        while l <= r:
            m = l + (r - l) // 2
           
            # check if m is valid. this means, can we scan the array greedily, limiting each subarray sum at m
            # and still finish the array in less than days scans?

            scans = 0
           
            right = 0
            while right < len(weights):
                sub_sum = 0
                while right < len(weights) and sub_sum + weights[right] <= m:
                    
                    sub_sum += weights[right]
                    right += 1
                
                
                scans += 1
       
            
            if scans <= days:
                # m is valid, so go into right half
                r = m - 1
            else:
                l = m + 1
        
        return l



        