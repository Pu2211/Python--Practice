class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right, min must be in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, min is in left half (including mid)
                right = mid
        
        # At the end, left == right pointing to the minimum
        return nums[left]
            