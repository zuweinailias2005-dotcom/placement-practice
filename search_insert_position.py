nums = [1,3,5,6]
target = 5

class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i]:
                return i
        
               


        

        
        