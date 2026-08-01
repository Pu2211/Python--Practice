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
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        res = float("-inf")
        # Iterate over left and right column boundaries
        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                # Update row sums for this column range
                for r in range(rows):
                    row_sums[r] += matrix[r][right]
                # Now find max subarray sum <= k for row_sums
                prefix_sums = [0]
                curr_sum = 0
                curr_max = float("-inf")
                for s in row_sums:
                    curr_sum += s
                    # We want smallest prefix >= curr_sum - k
                    idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                    if idx < len(prefix_sums):
                        curr_max = max(curr_max, curr_sum - prefix_sums[idx])
                    bisect.insort(prefix_sums, curr_sum)
                res = max(res, curr_max)
        return res
