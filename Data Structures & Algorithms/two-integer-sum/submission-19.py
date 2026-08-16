class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in map:
                map[nums[i]] = i
            else:
                return [map[diff], i]

            
