class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        
        # dp_score[r][c]: max score to reach cell (r, c) from (n - 1, n - 1). -1 means unreachable.
        # dp_count[r][c]: number of paths achieving dp_score[r][c]
        dp_score = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        # Base case: Start cell 'S' at (n - 1, n - 1)
        dp_score[n - 1][n - 1] = 0
        dp_count[n - 1][n - 1] = 1
        
        # Predecessor offsets when moving towards (0, 0)
        dirs = [(1, 0), (0, 1), (1, 1)]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == n - 1 and c == n - 1) or board[r][c] == 'X':
                    continue
                    
                val = 0 if board[r][c] == 'E' else int(board[r][c])
                
                max_prev_score = -1
                total_paths = 0
                
                for dr, dc in dirs:
                    pr, pc = r + dr, c + dc
                    # Check reachability using dp_score != -1 instead of dp_count > 0
                    if 0 <= pr < n and 0 <= pc < n and dp_score[pr][pc] != -1:
                        prev_score = dp_score[pr][pc]
                        if prev_score > max_prev_score:
                            max_prev_score = prev_score
                            total_paths = dp_count[pr][pc]
                        elif prev_score == max_prev_score:
                            total_paths = (total_paths + dp_count[pr][pc]) % MOD
                            
                if max_prev_score != -1:
                    dp_score[r][c] = max_prev_score + val
                    dp_count[r][c] = total_paths
                    
        if dp_score[0][0] == -1:
            return [0, 0]
            
        return [dp_score[0][0], dp_count[0][0]]