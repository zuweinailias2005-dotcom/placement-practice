head = [3,2,0,-4]
pos = 1

class Solution(object):
    def hasCycle(self, head):
        visited = set()
        current = head

        while current is not None:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False