from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Custom combination function nCr capped at `limit`
        # Compatible with all Python versions (Python 2.7, 3.6, 3.7, 3.8+)
        def comb(n, r, limit):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2:
                r = n - r
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= limit:
                    return limit
            return res

        # Helper function to compute distinct permutations of left-half characters
        def get_perms(counts_dict, limit):
            total = 1
            rem_len = sum(counts_dict.values())
            for c in counts_dict.values():
                if c > 0:
                    total *= comb(rem_len, c, limit)
                    rem_len -= c
                    if total >= limit:
                        return limit
            return total

        # Step 1: Count character frequencies in s
        counts = Counter(s)
        
        # Step 2: Extract half counts for the left half and locate middle character (if s has odd length)
        half_counts = {}
        mid_char = ""
        
        for ch, count in sorted(counts.items()):
            if count % 2 != 0:
                mid_char = ch
            half_counts[ch] = count // 2

        # Step 3: Check if total possible distinct palindromic permutations is less than k
        total_perms = get_perms(half_counts, k + 1)
        if total_perms < k:
            return ""
            
        # Step 4: Construct the left half character-by-character lexicographically
        left = []
        half_len = sum(half_counts.values())
        sorted_chars = sorted(half_counts.keys())
        
        for _ in range(half_len):
            for ch in sorted_chars:
                if half_counts[ch] > 0:
                    # Temporarily place character `ch` at current position
                    half_counts[ch] -= 1
                    perms = get_perms(half_counts, k)
                    
                    if k <= perms:
                        # Character `ch` belongs at this position
                        left.append(ch)
                        break
                    else:
                        # Skip `perms` possibilities and restore count of `ch`
                        k -= perms
                        half_counts[ch] += 1
                        
        left_str = "".join(left)
        
        # Step 5: Form the complete palindrome: left half + middle char + reversed left half
        return left_str + mid_char + left_str[::-1]