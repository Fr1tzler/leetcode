class Solution(object):
    def getKth(self, lo, hi, k):
        powers = dict()
        powers[1] = 0

        def power(x):
            if x in powers:
                return powers[x]
            if x % 2 == 0:
                next_state = power(x // 2)
                powers[x] = next_state + 1
                return powers[x]
            else:
                next_state = power(3 * x + 1)
                powers[x] = next_state + 1
                return powers[x]

        arr = list(range(lo, hi + 1))
        arr.sort(key=lambda x: power(x))
        return arr[k - 1]
        # quicksort partition is better