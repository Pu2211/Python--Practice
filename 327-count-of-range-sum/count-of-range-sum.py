class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Step 1: Build prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        # Step 2: Merge sort helper
        def sort_and_count(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort_and_count(lo, mid) + sort_and_count(mid, hi)
            j = k = mid
            for left_val in prefix[lo:mid]:
                while k < hi and prefix[k] - left_val < lower:
                    k += 1
                while j < hi and prefix[j] - left_val <= upper:
                    j += 1
                count += j - k
            # Merge step
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return sort_and_count(0, len(prefix))
