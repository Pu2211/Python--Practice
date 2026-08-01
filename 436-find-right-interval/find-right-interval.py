class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        import bisect
        # Step 1: Collect all interval starts with their original indices
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_points = [s[0] for s in starts]
        indices = [s[1] for s in starts]
        res = []
        # Step 2: For each interval, binary search for the smallest start >= its end
        for interval in intervals:
            end = interval[1]
            idx = bisect.bisect_left(start_points, end)
            if idx < len(start_points):
                res.append(indices[idx])
            else:
                res.append(-1)
        return res
