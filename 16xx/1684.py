class Solution(object):
    def countConsistentStrings(self, allowed, words):
        counter = 0
        for word in words:
            flag = True
            for char in word:
                if char not in allowed:
                    flag = False
            if flag:
                counter += 1
        return counter