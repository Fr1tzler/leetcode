class Solution(object):
    def removeDuplicates(self, S):
        res = []
        for char in S:
            if len(res) == 0:
                res.append(char)
            elif res[-1] == char:
                res.pop()
            else:
                res.append(char)
        return ''.join(res)
