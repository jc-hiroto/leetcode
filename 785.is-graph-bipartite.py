#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, colored = len(graph), {}
        def dfs_color(color, idx, graph, colored):
            if idx in colored:
                return color == colored[idx]
            colored[idx] = color                            
            return all(dfs_color(-color, neighbor, graph, colored) for neighbor in graph[idx])
    
        return all(i in colored or dfs_color(1, i, graph, colored) for i in range(n)) 
        
# @lc code=end

