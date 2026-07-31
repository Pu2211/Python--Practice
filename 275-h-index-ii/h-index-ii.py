class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Sort citations in descending order
        citations.sort(reverse=True)
        h = 0

        # Iterate through sorted citations
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break

        return h
