class Solution(object):
    def balancedStringSplit(self, s):
        balance = 0
        result = 0
        for i in s:
            if i == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                result += 1
        return result