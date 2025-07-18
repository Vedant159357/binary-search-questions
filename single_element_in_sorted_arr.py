class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low,high = 1, n-2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            #left half
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid + 1] == nums[mid]):
                low = mid + 1

            else:
                high = mid - 1

        return -1
