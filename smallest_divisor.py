import math
class Solution:
    def sumThreshold(self,nums,div):
        summ = 0
        for i in range(len(nums)):
            summ += math.ceil(nums[i] / div)
            
        return summ


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxi = max(nums)
        low,high = 1,maxi

        
        while low <= high:
            mid = (low + high) // 2
            if self.sumThreshold(nums,mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low


        
