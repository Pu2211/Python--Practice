class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to optimize binary search range to O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # Left and right boundary values around partition i in nums1
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            # Left and right boundary values around partition j in nums2
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # Valid partition condition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is odd
                if (m + n) % 2 != 0:
                    return float(max(maxLeft1, maxLeft2))
                # If total length is even
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            # Too many elements taken from nums1
            elif maxLeft1 > minRight2:
                high = i - 1
            # Too few elements taken from nums1
            else:
                low = i + 1
                
        return 0.0