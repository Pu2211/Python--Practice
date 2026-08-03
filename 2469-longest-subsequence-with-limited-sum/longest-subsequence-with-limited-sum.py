import bisect
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort nums to maximize subsequence length
        nums.sort()
        # Build prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        # For each query, find the largest prefix sum <= query
        result = []
        for q in queries:
            idx = bisect.bisect_right(prefix, q) - 1
            result.append(idx)
        return result