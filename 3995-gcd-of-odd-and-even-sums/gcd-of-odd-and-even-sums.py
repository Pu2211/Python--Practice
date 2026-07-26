from fractions import gcd
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_odd  = n * n        # Sum of first n odd numbers  = n²
        sum_even = n * (n + 1)  # Sum of first n even numbers = n(n+1)
        return gcd(sum_odd, sum_even)