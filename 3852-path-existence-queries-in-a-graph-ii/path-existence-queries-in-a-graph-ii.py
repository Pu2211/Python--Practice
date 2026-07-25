import bisect

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Extract sorted unique values and map them to 0-indexed positions
        vals = sorted(list(set(nums)))
        K = len(vals)
        val_to_idx = {val: i for i, val in enumerate(vals)}
        
        # Step 2: Build Binary Lifting table
        LOG = 18
        jump = [[0] * K for _ in range(LOG)]
        
        # Base jump of length 1 (2^0): furthest index reachable within maxDiff
        for i in range(K):
            m = bisect.bisect_right(vals, vals[i] + maxDiff) - 1
            jump[0][i] = m
            
        # Fill binary lifting table for 2^p steps
        for p in range(1, LOG):
            for i in range(K):
                jump[p][i] = jump[p - 1][jump[p - 1][i]]
                
        # Helper function to compute minimum steps from index i to j (i < j)
        def get_dist(i, j):
            if jump[LOG - 1][i] < j:
                return -1
            
            steps = 0
            curr = i
            for p in range(LOG - 1, -1, -1):
                if jump[p][curr] < j:
                    steps += (1 << p)
                    curr = jump[p][curr]
                    
            return steps + 1

        # Step 3: Answer each query
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            elif nums[u] == nums[v]:
                ans.append(1)
            else:
                i = val_to_idx[nums[u]]
                j = val_to_idx[nums[v]]
                if i > j:
                    i, j = j, i
                ans.append(get_dist(i, j))
                
        return ans