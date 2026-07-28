class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Base case for S1 = "0"
        if n == 1:
            return "0"
        
        # Calculate the middle position: 2^(n-1)
        mid = 1 << (n - 1)
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # k > mid: mirror position in S_(n-1) is (2^n - k)
            mirrored_bit = self.findKthBit(n - 1, (1 << n) - k)
            # Invert the bit
            return "1" if mirrored_bit == "0" else "0"