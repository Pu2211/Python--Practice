class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by start point ascending, and by end point descending for ties
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        prev_end = -1
        
        for start, end in intervals:
            # If the current interval extends beyond the max end seen so far,
            # it is NOT covered by any previous interval.
            if end > prev_end:
                count += 1
                prev_end = end
                
        return count