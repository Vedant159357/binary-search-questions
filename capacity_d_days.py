class Solution:
    def findDays(self,weights,cap):
        days,load = 1,0
        s = len(weights)
        for i in range(s):
            if (weights[i] + load) > cap:
                days += 1
                load = weights[i]
            else:
                load += weights[i]

        return days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            numberOfDays = self.findDays(weights,mid)

            if numberOfDays <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low
        
