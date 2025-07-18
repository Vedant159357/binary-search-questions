import math
class Solution:
    def totalHours(self,piles,hourly):
        total_hours = 0
        n = len(piles)
        for i in range(n):
            total_hours += math.ceil(piles[i] / hourly)
        return total_hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            total_hours = self.totalHours(piles,mid)
            
            if total_hours <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
        
