class Solution(object):
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(number):
            dividers = list(map(int, list(str(number))))
            for divider in dividers:
                if divider == 0:
                    return False
                if number % divider != 0:
                    return False   
            return True

        result = []
        for number in range(left, right + 1):
            if is_self_dividing(number):
                result.append(number)
        return result