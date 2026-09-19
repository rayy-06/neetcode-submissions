# Binary Search
# problems are in log(n) time. main algorithm applies to sorted arrays and halves the array
# on each search depending on if the target is larger or less than a midpoint element

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
       

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m

            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        