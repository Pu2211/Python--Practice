class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Coordinate compression
        sorted_unique = sorted(set(nums))
        ranks = {num: i+1 for i, num in enumerate(sorted_unique)}  # 1-indexed for BIT

        # Step 2: Fenwick Tree (BIT) implementation
        def update(bit, i, val):
            while i < len(bit):
                bit[i] += val
                i += i & -i

        def query(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        # Step 3: Traverse nums from right to left
        res = []
        bit = [0] * (len(ranks) + 1)

        for num in reversed(nums):
            rank = ranks[num]
            # Count of numbers smaller than current
            res.append(query(bit, rank - 1))
            # Add current number to BIT
            update(bit, rank, 1)

        return res[::-1]
