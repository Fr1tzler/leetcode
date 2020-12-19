# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        current = head
        while (l1 and l2):
            if l1.val > l2.val:
                current.next = ListNode(l2.val)
                l2 = l2.next
            else:
                current.next = ListNode(l1.val)
                l1 = l1.next
            current = current.next
        if l1:
            current.next = l1
        else:
            current.next = l2
        return head.next
        