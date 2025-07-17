class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2
            
            #if standing at the peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            #if standing at increasing curve
            elif nums[mid] > nums[mid - 1]:
                low = mid + 1

            #if standing at decreasing curve
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1

            else:#this case is when mid is at anti-peak means both left and right are greater
                low = mid + 1

        return - 1
