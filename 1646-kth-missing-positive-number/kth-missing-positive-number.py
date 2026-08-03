class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missing = 0
        current = 1
        idx = 0
        n = len(arr)
        # Iterate until we find the kth missing number
        while True:
            if idx < n and arr[idx] == current:
                idx += 1
            else:
                missing += 1
                if missing == k:
                    return current
            current += 1