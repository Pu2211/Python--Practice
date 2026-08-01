class SummaryRanges(object):
    def __init__(self):
        # Use a sorted list to store intervals
        self.intervals = []
    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        new_interval = [value, value]
        res = []
        placed = False
        for interval in self.intervals:
            if interval[1] + 1 < value:
                # Current interval ends before value
                res.append(interval)
            elif interval[0] - 1 > value:
                # Current interval starts after value
                if not placed:
                    res.append(new_interval)
                    placed = True
                res.append(interval)
            else:
                # Overlapping or adjacent intervals → merge
                new_interval[0] = min(new_interval[0], interval[0])
                new_interval[1] = max(new_interval[1], interval[1])
        if not placed:
            res.append(new_interval)
        self.intervals = res
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals
