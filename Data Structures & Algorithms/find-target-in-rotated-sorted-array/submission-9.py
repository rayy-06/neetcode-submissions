class Solution:
    def search(self, nums: List[int], target: int) -> int:
        split = self.findStart(nums)

        # 0 to split - 1 is first segment
        # split to len(nums) -1 is second segment

        # which half do we search into?
        r = len(nums) - 1

        if target == nums[r]:
            return r
        
        if target > nums[r]:
            l = 0
            r = split - 1
        else:
            l = split
            r = len(nums) - 1
        
        if split == 0:
            l = split
            r = len(nums) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid -1
            
            else:
                l = mid + 1
        
        return -1
    
    def findStart(self, nums: List[int]) -> int:        # this gives us the start of the second section
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return l

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # mid is in the right segment for sure
                if nums[mid] < nums[mid - 1]:
                    return mid
                else:
                    r = mid - 1
    
        