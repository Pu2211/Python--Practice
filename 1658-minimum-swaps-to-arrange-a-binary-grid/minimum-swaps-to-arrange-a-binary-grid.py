class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # Step 1: Count trailing zeros for each row
        zeros = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
            
        ans = 0
        
        # Step 2: Greedy selection for each row position i
        for i in range(n):
            needed = n - 1 - i
            
            # Find the closest valid row at or below index i
            found_idx = -1
            for j in range(i, n):
                if zeros[j] >= needed:
                    found_idx = j
                    break
            
            # If no valid row found, grid cannot be made valid
            if found_idx == -1:
                return -1
            
            # Add swaps required to move row found_idx to position i
            ans += (found_idx - i)
            
            # Move the selected row's count to position i
            val = zeros.pop(found_idx)
            zeros.insert(i, val)
            
        return ans