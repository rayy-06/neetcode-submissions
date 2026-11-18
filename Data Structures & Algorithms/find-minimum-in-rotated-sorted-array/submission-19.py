class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:   # wrong segment, so l is not the min for sure
                l = m + 1   
            else:
                r = m   # still partially correct segment, so dont rule out m
        return nums[r]