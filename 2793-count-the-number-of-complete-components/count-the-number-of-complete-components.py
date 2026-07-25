from collections import deque

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list for the undirected graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_count = 0
        
        # Step 2: Traverse each connected component
        for i in range(n):
            if not visited[i]:
                comp = []
                q = deque([i])
                visited[i] = True
                
                # BFS to collect all nodes in the current component
                while q:
                    u = q.popleft()
                    comp.append(u)
                    for neighbor in adj[u]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                            
                # Step 3: Check if every node in the component has degree == len(comp) - 1
                k = len(comp)
                if all(len(adj[node]) == k - 1 for node in comp):
                    complete_count += 1
                    
        return complete_count