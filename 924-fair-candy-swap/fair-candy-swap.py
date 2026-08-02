class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        # The difference each must adjust to balance
        diff = (sumA - sumB) // 2
        setB = set(bobSizes)
        for a in aliceSizes:
            b = a - diff
            if b in setB:
                return [a, b]