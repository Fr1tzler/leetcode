class Solution(object):
    def diStringMatch(self, S):
        min_elem, max_elem = 0, len(S)
        res = []
        for i in S:
            if i == "I":
                res.append(min_elem)
                min_elem += 1
            else:
                res.append(max_elem)
                max_elem -= 1
        res.append(max_elem)
        return res
            