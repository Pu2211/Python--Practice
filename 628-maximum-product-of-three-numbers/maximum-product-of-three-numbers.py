class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # Case 1: Three largest numbers
        case1 = nums[-1] * nums[-2] * nums[-3]
        # Case 2: Two smallest (most negative) × one largest
        case2 = nums[0] * nums[1] * nums[-1]
        return max(case1, case2)