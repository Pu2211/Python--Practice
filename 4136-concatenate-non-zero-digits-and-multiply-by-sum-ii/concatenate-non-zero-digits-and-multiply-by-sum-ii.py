class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        m = len(s)
        
        # 1. Precompute digit prefix sums
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + int(s[i])
            
        # 2. Extract non-zero digits and compute prefix values for x
        nz_count = [0] * (m + 1)
        non_zero_digits = []
        for i in range(m):
            if s[i] != '0':
                non_zero_digits.append(int(s[i]))
                nz_count[i + 1] = nz_count[i] + 1
            else:
                nz_count[i + 1] = nz_count[i]
                
        K = len(non_zero_digits)
        pref_x = [0] * (K + 1)
        for i in range(K):
            pref_x[i + 1] = (pref_x[i] * 10 + non_zero_digits[i]) % MOD
            
        # 3. Precompute powers of 10 modulo MOD
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # 4. Process each query in O(1) time
        ans = []
        for l, r in queries:
            A = nz_count[l]
            B = nz_count[r + 1] - 1
            
            if A > B:
                ans.append(0)
            else:
                N = B - A + 1
                x = (pref_x[B + 1] - pref_x[A] * pow10[N]) % MOD
                digit_sum = pref_sum[r + 1] - pref_sum[l]
                
                res = (x * digit_sum) % MOD
                ans.append(res)
                
        return ans