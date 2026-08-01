class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Helper function: check if we can split into <= k subarrays
        # with max subarray sum <= target
        def canSplit(target):
            count, curr_sum = 1, 0
            for num in nums:
                if curr_sum + num > target:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            return True
        # Binary search boundaries
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left

        