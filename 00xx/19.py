# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        def removeNode(head, n):
            if head == None:
                return 0
            val = removeNode(head.next, n)
            if val == n:
                head.next = head.next.next
            return val + 1
        
        head = ListNode(0, head)
        removeNode(head, n)
        return head.next
        