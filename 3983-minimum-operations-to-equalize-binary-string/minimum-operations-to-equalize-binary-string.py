from collections import deque
class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        initial_zeros = s.count('0')      
        # Already all 1s
        if initial_zeros == 0:
            return 0       
        # parent array for DSU to skip visited states with same parity
        parent = list(range(n + 3))      
        def find(i):
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i   
        dist = [-1] * (n + 1)
        dist[initial_zeros] = 0   
        # Mark initial_zeros as visited (skip to initial_zeros + 2)
        parent[initial_zeros] = find(initial_zeros + 2)
        queue = deque([initial_zeros])
        while queue:
            c = queue.popleft()
            if c == 0:
                return dist[c]
            # Valid range of zeros (x) we can flip
            x_min = max(0, k - n + c)
            x_max = min(c, k)
            if x_min > x_max:
                continue
            # Reachable range of new zero counts [L, R] with step size 2
            L = c + k - 2 * x_max
            R = c + k - 2 * x_min
            # Traverse unvisited zero counts in range [L, R]
            curr = find(L)
            while curr <= R:
                dist[curr] = dist[c] + 1
                if curr == 0:
                    return dist[curr]   
                queue.append(curr)
                # Mark curr as visited by linking to next state of same parity (curr + 2)
                parent[curr] = find(curr + 2)
                curr = find(curr)     
        return -1