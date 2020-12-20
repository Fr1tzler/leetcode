class Solution(object):
    def sortArrayByParityII(self, A):
        odd, even = [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        res = []
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        return res