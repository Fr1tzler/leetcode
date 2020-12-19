class Solution(object):
    def allPathsSourceTarget(self, graph):
        def DFS(graph, current_node):
            if current_node == len(graph) - 1:
                return [[current_node]]
            result = []
            for adjacent_vertex in graph[current_node]:
                for way in DFS(graph, adjacent_vertex):
                    result.append([current_node] + way)
            return result
        return DFS(graph, 0)
