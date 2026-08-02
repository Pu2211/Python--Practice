class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()     
        def is_valid(x):
            # Binary search to check if any element in arr2 is within distance d of x
            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2
                if abs(arr2[mid] - x) <= d:
                    return False
                if arr2[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return True
        count = 0
        for num in arr1:
            if is_valid(num):
                count += 1
        return count