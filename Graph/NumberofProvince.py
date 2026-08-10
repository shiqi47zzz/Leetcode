'''
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)

            for i in range(n):
                if (
                    isConnected[city][i] == 1 and i not in visited
                ):
                    dfs(i)

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        return provinces
