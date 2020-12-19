class Solution(object):
    def sortString(self, s):
        length = len(s)
        char_count = dict()
        chars = []
        for i in s:
            if i in char_count:
                char_count[i] += 1
            else:
                chars.append(i)
                char_count[i] = 1
        chars.sort()
        last_char = ''
        result = []
        while length:
            for char in chars:
                if char_count[char] > 0:
                    result.append(char)
                    char_count[char] -= 1
            chars.reverse()
            length -= 1
        return ''.join(result)