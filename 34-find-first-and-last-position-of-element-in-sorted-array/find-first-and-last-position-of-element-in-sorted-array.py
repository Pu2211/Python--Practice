class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_bound(is_first):
            lo, hi = 0, len(nums) - 1
            bound = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        hi = mid - 1   # keep searching left half
                    else:
                        lo = mid + 1   # keep searching right half
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return bound

        left = find_bound(True)
        if left == -1:
            return [-1, -1]
        right = find_bound(False)
        return [left, right]