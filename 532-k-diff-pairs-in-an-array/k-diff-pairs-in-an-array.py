class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        seen = set(nums)
        count = 0
        if k == 0:
            # Count numbers that appear more than once
            from collections import Counter
            freq = Counter(nums)
            for val in freq:
                if freq[val] > 1:
                    count += 1
        else:
            # Count unique pairs (x, x+k)
            for val in seen:
                if val + k in seen:
                    count += 1
        return count