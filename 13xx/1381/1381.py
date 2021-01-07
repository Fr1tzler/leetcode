class CustomStack(object):
    def __init__(self, maxSize):
        self.size = maxSize
        self.end = 0
        self.stack = [None for i in range(maxSize)]
        

    def push(self, x):
        if self.end == self.size:
            return
        self.stack[self.end] = x
        self.end += 1


    def pop(self):
        if self.end == 0:
            return -1
        self.end -= 1
        return self.stack[self.end]


    def increment(self, k, val):
        for i in range(min(k, self.end)):
            self.stack[i] += val