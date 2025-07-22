class Solution:
    def countStudents(self,nums,pages):
        students = 1
        pagesStudent = 0
        for i in range(len(nums)):
            if pagesStudent + nums[i] <= pages:
                pagesStudent += nums[i]
            else:
                students += 1
                pagesStudent = nums[i]

        return students



    def findPages(self, nums, m):
        if m > len(nums):
            return -1

        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2

            students = self.countStudents(nums,mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1

        return low

       
