from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # If the start or destination cell has a thief, safeness factor is 0
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
        
        # Step 1: Multi-source BFS to calculate min Manhattan distance 
        # from every cell to the nearest thief.
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        # Step 2: Helper function to verify if a path exists with safeness >= target
        def canReach(target):
            if dist[0][0] < target or dist[n - 1][n - 1] < target:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            bq = deque([(0, 0)])
            
            while bq:
                r, c = bq.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= target:
                        visited[nr][nc] = True
                        bq.append((nr, nc))
            return False

        # Step 3: Binary Search for the maximum safeness factor
        low, high = 0, min(dist[0][0], dist[n - 1][n - 1])
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans