class Solution(object):
    def numTeams(self, rating):
        result = 0
        for i in range(0, len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        result += 1
        return result