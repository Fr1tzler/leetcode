class Solution(object):
    def sortArrayByParity(self, A):
        odd = []
        even = []
        for elem in A:
            if elem % 2 == 0:
                even.append(elem)
            else:
                odd.append(elem)
        return even + odd