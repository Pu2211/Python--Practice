class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] = max score difference starting from index i

        # Fill dp from the end towards the start
        for i in range(n - 1, -1, -1):
            take, best = 0, float('-inf')
            # Alice can take 1, 2, or 3 stones
            for x in range(3):
                if i + x < n:
                    take += stoneValue[i + x]
                    best = max(best, take - dp[i + x + 1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
