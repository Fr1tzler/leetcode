class Solution(object):
    def deepestLeavesSum(self, root):
        from collections import deque
        queue = deque()
        queue.append([root, 0])
        nodes = []
        while len(queue) != 0:
            current = queue.popleft()
            if current[0] == None:
                continue
            nodes.append(current)
            queue.append([current[0].left, current[1] + 1])
            queue.append([current[0].right, current[1] + 1])
        max_height = 0
        for node in nodes:
            if node[1] > max_height:
                max_height = node[1]
        result = 0
        for node in nodes:
            if node[1] == max_height:
                result += node[0].val
        return result