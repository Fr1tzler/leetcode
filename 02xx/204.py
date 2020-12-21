class Solution(object):
    def countPrimes(self, n):
        def isPrime(number):
            i = 2
            while i * i <= number:
                if number % i == 0:
                    return False
                i += 1
            return True

        if n <= 1:
            return 0
        nums = [1 for number in range(n)]
        nums[0], nums[1] = 0, 0
        number = 2
        while number * number <= len(nums):
            if nums[number] == 1:
                if isPrime(number):
                    m = 2
                    while m * number < len(nums):
                        nums[m * number] = 0
                        m += 1
            number += 1
        return nums.count(1)
    