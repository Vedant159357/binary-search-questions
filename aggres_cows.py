class Solution:
    def canPlace(self,arr,dist,cows):
        cntCows = 1
        last = arr[0]
        for i in range(len(arr)):
            if arr[i] - last >= dist:
                cntCows += 1
                last = arr[i]

        if cntCows >= cows:
            return True
        else:
            return False

    def aggressiveCows(self, nums, k):
        nums.sort()
        n = len(nums)
        low = 1
        high = nums[n - 1] - nums[0]

        while low <= high:
            mid = (low + high) // 2

            if self.canPlace(nums,mid,k) == True:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return high

        
