class Solution(object):
    def toGoatLatin(self, S):
        words=S.split()
        result = []
        for i in range(len(words)):
            if words[i][0] in "aeiouAEIOU":
                result.append(words[i] + "maa" + i * 'a')
            else:
                result.append(words[i][1:] + words[i][0] + "maa" + i * 'a')
        return " ".join(result)
