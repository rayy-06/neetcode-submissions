class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        seen = set()
        for num in nums:
            seen.add(num)
        
        for num in nums:
            seq = 0
            if num - 1 not in seen:
                val = num
                while val in seen:
                    val += 1
                    seq += 1
                res = max(res, seq)
        return res

"""
at num, sequence starts if: num - 1 not in seen
sequence continues if: num - 1 in seen

then add num, and move. any time a new sequence starts, save the previous

ex.
[2, 20, 4, 10, 3, 4, 5]
"""
        