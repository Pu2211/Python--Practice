class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is less than the next element,
            # then the peak must be in the right half
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Otherwise, the peak is in the left half (including mid)
                right = mid

        # At the end, left == right pointing to a peak element
        return left
