class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Extract all non-zero digits as string characters
        digits = [ch for ch in str(n) if ch != '0']
        
        # If there are no non-zero digits (e.g. n = 0)
        if not digits:
            return 0
            
        # Form x by concatenating non-zero digits
        x = int("".join(digits))
        
        # Calculate the sum of non-zero digits
        digit_sum = sum(int(ch) for ch in digits)
        
        # Return x * sum
        return x * digit_sum