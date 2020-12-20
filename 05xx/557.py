class Solution(object):
    def reverseWords(self, s):
        res = s.split()
        for i in range(len(res)):
            res[i] = res[i][::-1]
        return ' '.join(res)