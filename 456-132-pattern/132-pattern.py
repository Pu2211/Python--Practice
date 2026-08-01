class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        stack = []
        third = float("-inf")  # This will represent the "2" in the 132 pattern
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if nums[i] < third:
                # Found a "1" smaller than the "2"
                return True
            while stack and nums[i] > stack[-1]:
                # Pop all smaller elements; the last popped is the best "2"
                third = stack.pop()
            stack.append(nums[i])
        return False