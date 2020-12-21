class Solution(object):
    def isHappy(self, n):
        def iterate(number):
            s = map(int, list(str(number)))
            res = 0
            for i in s:
                res += i * i
            return res

        visited = set()
        while n not in visited and n != 1:
            visited.add(n)
            n = iterate(n)
        return n == 1