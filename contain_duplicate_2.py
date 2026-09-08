nums = [1,2,3,1]
k = 3

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        seen = {}

        for i in range(len(nums)):

            if nums[i] in seen:

                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False