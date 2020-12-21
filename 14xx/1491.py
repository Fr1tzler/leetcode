class Solution(object):
    def average(self, salary):
        min_salary = min(salary)
        max_salary = max(salary)
        return float(sum(salary) - min_salary - max_salary) / (len(salary) - 2)