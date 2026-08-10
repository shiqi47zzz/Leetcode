'''
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                result.append(path.copy())
                return
            
            for i in graph[node]:
                path.append(i)
                dfs(i, path)
                path.pop()

        dfs(0, [0])
        return result