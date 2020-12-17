class Solution(object):
    def subtractProductAndSum(self, n):
        lst = list(map(int, list(str(n))))
        product = 1
        for i in lst:
            product *= i
        return product - sum(lst)