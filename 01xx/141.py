class Solution(object):
    def hasCycle(self, head):
        visited = []
        while head:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False