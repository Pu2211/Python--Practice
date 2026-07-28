class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # The answer is simply the maximum digit in string n converted to an integer
        return int(max(n))