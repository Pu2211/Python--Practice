import random
import bisect
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total
    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.total)
        # Binary search to find the index corresponding to target
        idx = bisect.bisect_left(self.prefix_sums, target)
        return idx