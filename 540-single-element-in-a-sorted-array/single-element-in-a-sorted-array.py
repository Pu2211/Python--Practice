class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary search approach: O(log n) time, O(1) space
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Ensure mid is even for easier pairing
            if mid % 2 == 1:
                mid -= 1
            # If pair is valid, move right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]