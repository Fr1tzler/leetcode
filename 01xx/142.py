class Solution(object):
    def detectCycle(self, head):
        visited = []
        while head:
            if head in visited:
                return head
            visited.append(head)
            head = head.next