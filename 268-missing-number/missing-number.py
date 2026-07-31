class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        # Actual sum of given numbers
        actual_sum = sum(nums)
        # The missing number is the difference
        return expected_sum - actual_sum
