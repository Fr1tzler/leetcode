# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        lesser_head = ListNode()
        lesser = lesser_head
        greater_head = ListNode()
        greater = greater_head
        current = head

        while current:
            if current.val < x:
                lesser.next = current
                lesser = lesser.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        lesser.next = greater_head.next
        greater.next = None
        return lesser_head.next
