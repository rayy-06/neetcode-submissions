class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the segment which the target is inside
        target_in_r = 0 # 0 means its false, (in left), 1 means true (in right)
        if target <= nums[-1]:
            target_in_r = 1
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            m_in_r = 0
            if nums[m] < nums[-1]:
                m_in_r = 1
            
            if m_in_r == target_in_r:
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # target in right, m in left
                if target_in_r > m_in_r:
                    l = m + 1
                else:
                    r = m - 1
        return -1

         