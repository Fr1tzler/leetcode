class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        counter = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                counter += 1
        return counter