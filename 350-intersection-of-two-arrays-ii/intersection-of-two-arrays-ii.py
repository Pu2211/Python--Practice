class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        # Count occurrences in both arrays
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)

        result = []

        # For each number in counts1, add the minimum occurrence from both arrays
        for num in counts1:
            if num in counts2:
                result.extend([num] * min(counts1[num], counts2[num]))

        return result
