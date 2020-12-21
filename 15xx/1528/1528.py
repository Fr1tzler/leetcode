class Solution(object):
    def restoreString(self, s, indices):
        result = list(s)
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        return ''.join(result)