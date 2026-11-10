class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i
            
            needed = target - nums[i]
            if needed in map and map[needed] != i:
                return [
                    map[needed],
                    i
                ]
