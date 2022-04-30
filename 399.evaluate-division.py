#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def dfs(self, start, end, visited, res):
        if start not in self.graph:
            return -1.0
        if start == end:
            return res
        visited.add(start)
        for node in self.graph[start]:
            if node not in visited:
                new_res = self.dfs(node, end, visited, res * self.graph[start][node])
                if new_res != -1.0:
                    return new_res
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = {}
        ans = []
        for equation in equations:
            self.graph[equation[0]] = self.graph.get(equation[0], {})
            self.graph[equation[1]] = self.graph.get(equation[1], {})
            self.graph[equation[0]][equation[1]] = values[equations.index(equation)]
            self.graph[equation[1]][equation[0]] = 1 / values[equations.index(equation)]
        for query in queries:
            if query[0] not in self.graph or query[1] not in self.graph:
                ans.append(-1.0)
                continue
            ans.append(self.dfs(query[0], query[1], set(), 1.0))
        return ans

# @lc code=end

