class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        import math
        n = int(n)
        # The maximum possible length of representation is log2(n)
        max_m = int(math.log(n, 2))
        # Try lengths from max_m down to 2
        for m in range(max_m, 1, -1):
            # Binary search for base k
            left, right = 2, int(n ** (1.0 / m)) + 1
            while left <= right:
                mid = (left + right) // 2
                # Compute sum of geometric series: 1 + mid + mid^2 + ... + mid^m
                total = (mid ** (m + 1) - 1) // (mid - 1)
                if total == n:
                    return str(mid)
                elif total < n:
                    left = mid + 1
                else:
                    right = mid - 1
        # If no smaller base found, answer is n-1 (representation "11")
        return str(n - 1)
