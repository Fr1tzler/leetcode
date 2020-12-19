class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        first_part = list1
        while a - 1:
            a -= 1
            b -= 1
            first_part = first_part.next
        second_part = first_part.next
        while b:
            b -= 1
            second_part = second_part.next
        first_part.next = list2
        node = first_part
        while node.next:
            node = node.next
        node.next = second_part
        return list1
