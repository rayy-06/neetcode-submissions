class Solution:
    def isValid(self, num_string):
        if num_string[0] == "0":
            return False
        return int(num_string) <= 26 and int(num_string) > 0

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            return 1
        
        dp = [0] * len(s)       # dp[i] denotes the number of valid translations of s until index i
        dp[0] = 1
        if self.isValid(s[0] + s[1]) and s[1] != "0":
            dp[1] = 2
        elif not self.isValid(s[0] + s[1]) and s[1] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
        

        for i in range(2, len(s)):
            cand = s[i-1] + s[i]
            if s[i] == "0" and self.isValid(cand):     # char not 0, and cand valid
                dp[i] = dp[i-2]

            elif s[i] != "0" and self.isValid(cand):
                dp[i] = dp[i-1] + dp[i-2]
            
            elif s[i] != "0" and not self.isValid(cand):
                dp[i] = dp[i-1]

            else: # s[i] == 0 and invalid
                dp[i] = 0
        print(dp)
            
        return dp[len(s) - 1]



        