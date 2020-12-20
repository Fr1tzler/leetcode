class Solution(object):
    def minSteps(self, s, t):
        char_dict = dict()
        for char in set(s):
            char_dict[char] = s.count(char)
        for char in set(t):
            if char in char_dict:
                char_dict[char] -= t.count(char)
            else:
                char_dict[char] = t.count(char)
        res = 0
        for char in char_dict:
            res += abs(char_dict[char])
        return res // 2
