class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # In the classic Stone Game problem, Alex always wins if both play optimally.
        # Reason: The number of piles is even, so Alex can always choose either all odd-indexed
        # or all even-indexed piles, whichever has the larger total.
        return True     