class Solution(object):
    def buildArray(self, target, n):
        current_num = 0
        res = []
        for i in target:
            while current_num + 1 != i:
                res.append("Push")
                res.append("Pop")
                current_num += 1
            res.append("Push")
            current_num += 1
        return res