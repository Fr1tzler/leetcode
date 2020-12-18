class Solution(object):
    def getAllElements(self, root1, root2):
        def BFS(root):
            from collections import deque
            queue = deque()
            queue.append(root)
            result = []
            while len(queue) != 0:
                current = queue.popleft()
                if current == None:
                    continue
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            return result
        
        lst = BFS(root1) + BFS(root2)
        lst.sort()
        return lst