class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        rows, cols = len(grid), len(grid[0])
        r, c = rows - 1, 0  # start from bottom-left corner
        # Since each row is sorted in non-increasing order,
        # we can use a staircase search to count negatives efficiently.
        while r >= 0 and c < cols:
            if grid[r][c] < 0:
                # All elements to the right of grid[r][c] are also negative
                count += (cols - c)
                r -= 1
            else:
                c += 1
        return count