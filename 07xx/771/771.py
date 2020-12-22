class Solution(object):
    def numJewelsInStones(self, J, S):
        jewels = set(J)
        counter = 0
        for i in S:
            if i in jewels:
                counter += 1
        return counter
