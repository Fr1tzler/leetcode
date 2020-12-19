class Solution(object):
    def getDecimalValue(self, head):
        result = 0
        node = head
        while node:
            result = result * 2 + node.val
            node = node.next
        return result