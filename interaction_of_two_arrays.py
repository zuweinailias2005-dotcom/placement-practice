nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution(object):
    def intersection(self, nums1, nums2):

        set1 = set(nums1)
        result = set()

        for n in nums2:
            if n in set1:
                result.add(n)
        return list(result)
