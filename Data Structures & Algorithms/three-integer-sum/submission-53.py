class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # on each iteration, fix a number and run two pointer two sum algo on the rest
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l <= r:
                cand = nums[i] + nums[l] + nums[r]
                if cand == 0 and len({i, l, r}) == 3:
                    res.append([nums[i], nums[l], nums[r]])
                    last_l = nums[l]
                    last_r = nums[r]
                    while l < r and nums[l] == last_l:
                        l += 1
                    while l < r and nums[r] == last_r:
                        r -= 1
                elif cand < 0:
                    l += 1
                else:
                    r -= 1
        return res

        