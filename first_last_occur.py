class Solution:
    def firstOccurance(self,nums,target):
        n = len(nums)
        low,high = 0, n -1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return first

    def lastOccurance(self,nums,target):
        n = len(nums)
        low,high = 0, n -1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return last



    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = self.firstOccurance(nums,target)
        if first_index == -1:
            return [-1,-1]
        last_index = self.lastOccurance(nums,target)

        return [first_index, last_index]

        
        
        
