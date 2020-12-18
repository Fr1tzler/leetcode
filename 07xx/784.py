class Solution(object):
    def letterCasePermutation(self, S):
        if len(S) == 1:
            return [S.lower, S.upper]
        res2 = []
        j = self.letterCasePermutation(S[1:])
        for i in j:
            res2.append(S[0].lower + j)
            res2.append(S[0].upper + j)
        return list(set(res2))