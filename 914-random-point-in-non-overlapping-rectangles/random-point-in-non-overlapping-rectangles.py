import random
import bisect
class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.weights = []
        total = 0
        for x1, y1, x2, y2 in rects:
            # Number of integer points in this rectangle
            count = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += count
            self.weights.append(total)
        self.total = total
    def pick(self):
        """
        :rtype: List[int]
        """
        # Randomly select a rectangle weighted by its area
        target = random.randint(1, self.total)
        idx = bisect.bisect_left(self.weights, target)
        x1, y1, x2, y2 = self.rects[idx]
        # Pick a random point inside the chosen rectangle
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]