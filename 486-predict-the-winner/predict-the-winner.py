class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}

        def score(left, right):
            # Base case: only one number left
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            # Player chooses left or right optimally
            pick_left = nums[left] - score(left + 1, right)
            pick_right = nums[right] - score(left, right - 1)

            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        # If Player 1's score difference >= 0, they can win or tie
        return score(0, len(nums) - 1) >= 0
