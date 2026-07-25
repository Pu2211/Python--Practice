class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Step 1: Extract sorted unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a mapping of element -> rank (1-indexed)
        rank_map = {val: rank + 1 for rank, val in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[val] for val in arr]