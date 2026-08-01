class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Step 1: Identify the digit length group
        length = 1
        count = 9
        start = 1
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        # Step 2: Find the actual number containing the nth digit
        num = start + (n - 1) // length
        # Step 3: Find the digit within that number
        digit_index = (n - 1) % length
        return int(str(num)[digit_index])
