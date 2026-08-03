class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        # Two-pointer approach
        while left < right:
            if nums[left] + nums[right] < target:
                # All pairs with nums[left] and elements between left+1..right are valid
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count