class Solution(object):
    def uniqueOccurrences(self, arr):
        occurencies_count = dict()
        for i in arr:
            if i in occurencies_count:
                occurencies_count[i] += 1
            else:
                occurencies_count[i] = 1
        occurencies = []
        for i in occurencies_count:
            occurencies.append(occurencies_count[i])
        return len(occurencies) == len(set(occurencies))
