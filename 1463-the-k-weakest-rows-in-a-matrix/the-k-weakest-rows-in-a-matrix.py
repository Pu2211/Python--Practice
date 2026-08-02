class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Count soldiers (1s) in each row and pair with row index
        strength = [(sum(row), idx) for idx, row in enumerate(mat)]      
        # Sort by soldier count, then by row index
        strength.sort(key=lambda x: (x[0], x[1]))
        # Extract the indices of the k weakest rows
        return [idx for _, idx in strength[:k]]       