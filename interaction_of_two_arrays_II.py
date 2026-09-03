nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution(object):
    def intersect(self, nums1, nums2):

        count = {}
        result = []

        for n in nums1:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        for n in nums2:
            if n in count and count[n] > 0:
                result.append(n)
                count[n] -= 1
        return result




            
        
        