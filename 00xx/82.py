# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        head = ListNode(None, head)
        current = head.next
        prev = head
        while current:
            if current.next and current.next.val == current.val:
                while current.next and current.next.val == current.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return head.next