class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        unreachable = set(range(n))
        for edge in edges:
            if edge[1] in unreachable:
                unreachable.remove(edge[1])
        return sorted(list(unreachable))
