class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = None
        res_curr = None
        l1_curr = l1
        l2_curr = l2
        acc = 0
        while l1_curr and l2_curr:
            value = l1_curr.val + l2_curr.val + acc
            acc = 0
            if value >= 10:
                acc = value // 10
                value %= 10
            if result == None:
                result = ListNode(value)
                res_curr = result
            else:
                res_curr.next = ListNode(value)
                res_curr = res_curr.next
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
        node = l1_curr
        if l2_curr != None:
            node = l2_curr
        while node:
            value = node.val + acc
            acc = 0
            if value >= 10:
                acc = value // 10
                value %= 10
            res_curr.next = ListNode(value)
            res_curr = res_curr.next
            node = node.next
        if acc != 0:
            res_curr.next = ListNode(acc)
        return result
    