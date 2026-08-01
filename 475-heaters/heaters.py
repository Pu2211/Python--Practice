class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        import bisect
        # Sort heaters for binary search
        heaters.sort()
        res = 0
        for house in houses:
            # Find insertion position of house in heaters
            idx = bisect.bisect_left(heaters, house)
            # Distance to nearest heater on the left
            left_dist = float("inf") if idx == 0 else house - heaters[idx - 1]
            # Distance to nearest heater on the right
            right_dist = float("inf") if idx == len(heaters) else heaters[idx] - house
            # Minimum distance for this house
            nearest = min(left_dist, right_dist)
            # Update maximum radius needed
            res = max(res, nearest)
        return res

        