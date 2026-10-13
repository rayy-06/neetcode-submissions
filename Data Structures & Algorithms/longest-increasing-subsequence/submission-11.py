class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        dp = [0] * len(nums)
        dp[0] = 1
        dp[1] = 2 if nums[1] > nums[0] else 1

        if len(nums) == 2:
            return max(dp[0], dp[1])

        res = 0

        for i in range(2, len(nums)):
            k = i   # start a pointer to go backwards
            ans = -1
            while k > 0:
                k -= 1
                if nums[k] < nums[i]:   # we can only increment if the element before was part of the actual LIS seen
                    ans = max(dp[k] + 1, ans)

            dp[i] = 1 if ans == -1 else ans
            res = max(dp[i], res)
        
        return res
                
        