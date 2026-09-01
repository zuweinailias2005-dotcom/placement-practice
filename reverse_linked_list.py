head = [1,2,3,4,5]

class Solution(object):
    def reverseList(self,head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev