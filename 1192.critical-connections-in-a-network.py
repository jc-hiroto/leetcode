#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (52.07%)
# Likes:    4490
# Dislikes: 162
# Total Accepted:    174.2K
# Total Submissions: 321.1K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n - 1 connected by undirected
# server-to-server connections forming a network where connections[i] = [ai,
# bi] represents a connection between servers ai and bi. Any server can reach
# other servers directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some
# servers unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^5
# n - 1 <= connections.length <= 10^5
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def dfs(rank, node, prevNode):
            res = []
            lows[node] = rank
            for nextNode in graph[node]:
                if nextNode == prevNode:
                    continue

                if not lows[nextNode]:
                    res += dfs(rank+1, nextNode, node)

                lows[node] = min(lows[node], lows[nextNode])

                if lows[nextNode] >= rank+1:
                    res.append([node, nextNode])
            return res

        graph = defaultdict(list)
        lows = [0] * n
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        res = dfs(1, 0, -1)
        return res
    
            # @lc code=end

