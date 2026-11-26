class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        scan and land start off from the end on which we want to pack the elements
        the elements we choose to pack will keep their order (ie. zero vs non zero)

        so, we start both pointers on right and "pack" non zero elements to the right
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:    # if we hit an element we need to shift/pack to end
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        

        