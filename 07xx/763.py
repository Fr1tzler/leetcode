class Solution(object):
    def partitionLabels(self, S):
        strings = []
        while (len(S) != 0):
            elem = S[0]
            last_occurence = S.rindex(elem)
            iter = 0
            while iter < last_occurence:
                iter += 1
                if S.rfind(S[iter]) > last_occurence:
                    last_occurence = S.rfind(S[iter])
            strings.append(last_occurence + 1)
            S = S[last_occurence + 1 : ]
        return strings