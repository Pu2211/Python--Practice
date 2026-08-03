class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Sort the array first
        nums.sort()
        
        # Collect indices where nums[i] == target
        result = []
        for i, val in enumerate(nums):
            if val == target:
                result.append(i)
        return result