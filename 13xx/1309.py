class Solution(object):
    def freqAlphabets(self, s):
        res = []
        s = s + '__'
        i = 0
        while (i < len(s) - 2):
            if s[i + 2] == '#':
                res.append(chr(int(s[i:i+2]) + 96))
                i += 1
            elif s[i] != '#':
                res.append(chr(int(s[i]) + 96))
            i += 1
        return ''.join(res)