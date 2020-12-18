class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        def find_way_to_target(root, target):
            from collections import deque
            search_queue = deque()
            search_queue.append((root,''))
            while len(search_queue) != 0:
                current = search_queue.popleft()
                if current[0] == None:
                    continue
                if current[0] == target:
                    return current[1]
                search_queue.append((current[0].left, current[1] + "L"))
                search_queue.append((current[0].right, current[1] + "R"))
        
        def get_target_link(root, way):
            node = root
            for i in way:
                if i == "L":
                    node = node.left
                else:
                    node = node.right
            return node

        return get_target_link(cloned, find_way_to_target(original, target))        
