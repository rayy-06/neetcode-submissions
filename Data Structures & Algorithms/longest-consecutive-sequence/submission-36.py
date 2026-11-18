class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        seen = set()    # pre process into a set
        for num in nums:
            seen.add(num)
        
        for num in nums:    # we would technically check for a sequence off of each num
            seq = 0            # cannot rely on ordering
            if num - 1 not in seen: # add one check: only start counting for nums which are actually a start of a sequence
                val = num
                while val in seen:
                    val += 1
                    seq += 1
                res = max(res, seq)
        return res
        