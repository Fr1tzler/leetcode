class Solution(object):
    def oddEvenList(self, head):
        even_start = None
        odd_start = None
        even_curr = None
        odd_curr = None
        current = head
        even = False
        while current:
            if even:
                if even_start == None:
                    even_start = current
                    even_curr = current
                else:
                    even_curr.next = current
                    even_curr = current
            else:
                if odd_start == None:
                    odd_start = current
                    odd_curr = current
                else:
                    odd_curr.next = current
                    odd_curr = current
            even = not even
            current = current.next
        if odd_curr:
            odd_curr.next = even_start
        if even_curr:
            even_curr.next = None
        return odd_start                