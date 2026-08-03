class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        n = len(nums)

        for x in range(1, n + 1):
            # Count how many numbers are >= x
            if nums[x - 1] >= x and (x == n or nums[x] < x):
                return x
        return -1
