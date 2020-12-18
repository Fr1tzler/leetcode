class Solution(object):
    def middleNode(self, head):
        node1, node2 = head, head
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
        return node1
