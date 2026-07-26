class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        MOD = 10**9 + 7
        max_v = max(nums)
        
        gcd_table = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        for i in range(max_v + 1):
            for j in range(max_v + 1):
                if i == 0:
                    gcd_table[i][j] = j
                elif j == 0:
                    gcd_table[i][j] = i
                else:
                    gcd_table[i][j] = gcd(i, j)
                    
        dp = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        dp[0][0] = 1
        
        for x in nums:
            next_dp = [row[:] for row in dp]
            for g1 in range(max_v + 1):
                for g2 in range(max_v + 1):
                    count = dp[g1][g2]
                    if count == 0:
                        continue
                    
                    ng1 = gcd_table[g1][x]
                    next_dp[ng1][g2] = (next_dp[ng1][g2] + count) % MOD
                    
                    ng2 = gcd_table[g2][x]
                    next_dp[g1][ng2] = (next_dp[g1][ng2] + count) % MOD
                    
            dp = next_dp
            
        ans = 0
        for g in range(1, max_v + 1):
            ans = (ans + dp[g][g]) % MOD
            
        return ans