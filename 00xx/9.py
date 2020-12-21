class Solution(object):
    def isPalindrome(self, x):
        s1 = str(x)
        return s1 == s1[::-1]