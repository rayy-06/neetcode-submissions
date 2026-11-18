class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        target_in_r = target <= nums[-1]

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            m_in_r = nums[m] <= nums[-1]
            if m_in_r == target_in_r: # same segment, original comparisons
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else: # different segments. if target in r, m in l and vv
                if target_in_r:
                    l = m + 1
                else:
                    r = m - 1
        return -1


            

"""
Main Idea: a rotated sorted array gets split into two sorted segments (as we saw in find min, rotated sorted array). If we use Binary search and find m, we boil into two cases.

1) The target, and m are in the same segment. If so, this is a regular binary search problem. Do not do anything different (ie. still compare nums[m], target and adjust l, r accordingly)

2) The target and m are in different segments. Our goal is to get into case (1), meaning we try to force m to fall into the same segment as target on next run. How? Push the corresponding endpoint. 
ie. if m is in left but target in right, l = m + 1

This is done with a few tools
- booleans tracking the position of the target relative to the segments (fixed) and a boolean calculated at iteration, checking which segment m is in
- compare (nums[m], nums[-1]) and (target, nums[-1]) for each of these booleans



"""

         