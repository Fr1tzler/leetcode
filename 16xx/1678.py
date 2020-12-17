import re

class Solution(object):
    def interpret(self, command):
        result = re.sub(r'\(al\)', 'al', command)
        return re.sub(r'\(\)', 'o', result)