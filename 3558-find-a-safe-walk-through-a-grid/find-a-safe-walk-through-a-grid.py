from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # dist[r][c] stores the minimum health loss to reach cell (r, c)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        
        # 0-1 BFS since cost to enter a cell is either 0 or 1
        q = deque([(0, 0)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            
            # Optimization: stop early when popping destination cell
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        if cost == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
                            
        # Final health must be >= 1, meaning health lost must be <= health - 1
        return dist[m - 1][n - 1] <= health - 1