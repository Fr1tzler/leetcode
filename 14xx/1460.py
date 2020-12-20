class Solution(object):
    def canBeEqual(self, target, arr):
        for i in set(target):
            if target.count(i) != arr.count(i):
                return False
        return True