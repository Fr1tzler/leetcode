class Solution(object):
    def convertToTitle(self, n):
        res = []
        while n > 0:
            char_id = n % 26
            if char_id == 0:
                char_id = 26
            res.append(chr(char_id - 1 + ord("A")))
            n = (n - char_id) // 26
        res.reverse()
        return ''.join(res)
