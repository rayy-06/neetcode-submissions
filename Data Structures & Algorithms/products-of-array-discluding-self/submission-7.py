class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):  # go backwards starting at the second last num, up until -1 (so stop at 0th number)
            suff[i] = suff[i + 1] * nums[i + 1]

        return [
            pre[i] * suff[i] for i in range(len(nums))
        ]

        