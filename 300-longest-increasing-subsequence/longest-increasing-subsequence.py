class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect

        sub = []  # will store the increasing subsequence

        for num in nums:
            # Find the index where num should be placed
            idx = bisect.bisect_left(sub, num)

            # If num is greater than all elements in sub, append it
            if idx == len(sub):
                sub.append(num)
            else:
                # Otherwise, replace the element at idx
                sub[idx] = num

        return len(sub)
