nums = [1,2,3,1]
class Solution(object):
    def containsDuplicate(self, nums):
        arr = set()
        for n in nums:
            if n in arr:
                return True
            arr.add(n)
        return False