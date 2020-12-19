class OrderedStream(object):
    def __init__(self, n):
        self.stream = [None for i in range(n + 2)]
        self.last = 0
        

    def insert(self, id, value):
        self.stream[id][0] = value
        if id - 1 == self.last:
            result = []
            current_id = id
            while self.stream[current_id]:
                result.append(self.stream[current_id])
                current_id += 1
            self.last = current_id - 1
            return result