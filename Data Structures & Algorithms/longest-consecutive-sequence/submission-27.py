class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in seen: # it is a valid start
                seq = 1
                n = nums[i]
                while n + 1 in seen:
                    seq += 1
                    n += 1
                longest = max(seq, longest)
        return longest
        