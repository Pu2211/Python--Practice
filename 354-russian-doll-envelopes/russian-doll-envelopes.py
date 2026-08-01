class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect
        # Step 1: Sort envelopes
        # Sort by width ascending, and if widths are equal, sort by height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # Step 2: Extract heights
        heights = [h for _, h in envelopes]
        # Step 3: Find LIS on heights
        sub = []
        for h in heights:
            idx = bisect.bisect_left(sub, h)
            if idx == len(sub):
                sub.append(h)
            else:
                sub[idx] = h
        return len(sub)

        