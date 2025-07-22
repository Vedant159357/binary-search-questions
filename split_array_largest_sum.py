class Solution:
    def possible(self,nums,k,target):
        count = 1
        summ = 0
        for i in range(len(nums)):
            if nums[i] > target:
                return False
            if (summ + nums[i] > target):
                count += 1
                summ = nums[i]
            else:
                summ += nums[i]

        return count <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.possible(nums,k,mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans 
        
