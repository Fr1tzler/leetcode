class Solution(object):
    def repeatedNTimes(self, A):
        appeared = set()
        for i in A:
            if i not in appeared:
                appeared.add(i)
            else:
                return i