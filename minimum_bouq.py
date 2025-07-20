class Solution:
    def possible(self,bloomDay,day,m,k):
        cnt = 0
        numberOfBouq = 0
        n = len(bloomDay)
        for i in range(n):
            if bloomDay[i] <= day:
                cnt += 1
                if cnt == k:
                    numberOfBouq += 1
                    cnt = 0
            else:
                cnt = 0

        return numberOfBouq >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low,high = min(bloomDay),max(bloomDay)
        total_flowers = m * k
        if total_flowers > len(bloomDay):
            return - 1

        ans = -1
        while low <= high:
            mid = (low + high) // 2

            if self.possible(bloomDay,mid,m,k) == True:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        
