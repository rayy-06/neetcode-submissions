class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum array: pre[i] = sum of elements until nums[i]

        pre = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        suf = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]

        return [(pre[i] * suf[i]) for i in range(len(nums))]
"""
        [1, 2, 4, 6]
        [48,24, 6,1]
        [1, 1,  2, 8]
        """


        