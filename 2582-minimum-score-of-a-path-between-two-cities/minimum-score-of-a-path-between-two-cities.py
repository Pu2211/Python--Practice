from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the graph adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # Step 2: Traverse the connected component starting from city 1 using BFS
        visited = [False] * (n + 1)
        visited[1] = True
        
        q = deque([1])
        min_score = float('inf')
        
        while q:
            u = q.popleft()
            for v, w in adj[u]:
                # Update minimum edge weight in this component
                min_score = min(min_score, w)
                
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    
        return min_score