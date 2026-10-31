class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        i = 0
        for i in range(len(nums)):  # keep this one fixed outside
            j = i + 1
            k = len(nums) - 1
            while j < k:    # start two pointers with their OWN loop
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:   # only add the triplet if it is unqiue
                        result.append(triplet)
                    j += 1
                    k -= 1
        
        return result
        