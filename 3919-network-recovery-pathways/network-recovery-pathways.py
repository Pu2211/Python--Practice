from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        
        # Build adjacency list and calculate in-degrees for topological sort
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs = set()
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            unique_costs.add(cost)
            
        if not unique_costs:
            return -1
            
        sorted_costs = sorted(list(unique_costs))
        
        # Step 1: Compute Topological Order using Kahn's Algorithm
        q = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        # Step 2: Helper function to check if a valid path exists with min edge cost >= S
        def check(S):
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                # Skip unreachable nodes, nodes exceeding cost limit k, or offline nodes
                if dist[u] > k or not online[u]:
                    continue
                for v, cost in adj[u]:
                    if cost >= S and online[v]:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            
            return dist[n - 1] <= k

        # Step 3: Binary Search over sorted unique edge costs
        low, high = 0, len(sorted_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(sorted_costs[mid]):
                ans = sorted_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans