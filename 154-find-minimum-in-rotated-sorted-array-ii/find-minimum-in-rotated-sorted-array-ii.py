class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than right, min must be in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is smaller than right, min must be in left half (including mid)
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # When nums[mid] == nums[right], we cannot decide, so shrink right
                right -= 1

        return nums[left]
