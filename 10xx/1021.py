class Solution(object):
    def removeOuterParentheses(self, S):
        balance = 0
        res = []
        for i in S:
            if i == '(':
                balance += 1
                if balance == 1:
                    continue
            else:
                balance -= 1
                if balance == 0:
                    continue
            res.append(i)
        return ''.join(res)