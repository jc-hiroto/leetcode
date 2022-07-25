/*
 * @lc app=leetcode id=547 lang=cpp
 *
 * [547] Number of Provinces
 *
 * https://leetcode.com/problems/number-of-provinces/description/
 *
 * algorithms
 * Medium (62.59%)
 * Likes:    5619
 * Dislikes: 247
 * Total Accepted:    499.3K
 * Total Submissions: 794.5K
 * Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
 *
 * There are n cities. Some of them are connected, while some are not. If city
 * a is connected directly with city b, and city b is connected directly with
 * city c, then city a is connected indirectly with city c.
 *
 * A province is a group of directly or indirectly connected cities and no
 * other cities outside of the group.
 *
 * You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
 * i^th city and the j^th city are directly connected, and isConnected[i][j] =
 * 0 otherwise.
 *
 * Return the total number of provinces.
 *
 *
 * Example 1:
 *
 *
 * Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 200
 * n == isConnected.length
 * n == isConnected[i].length
 * isConnected[i][j] is 1 or 0.
 * isConnected[i][i] == 1
 * isConnected[i][j] == isConnected[j][i]
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int findCircleNum(vector<vector<int>>& nodeMap) {
        int res = 0;
        unordered_set<int> visited;
        for (int i = 0; i < nodeMap.size(); i++) {
            if (visited.find(i) == visited.end()) {
                res++;
                visited.insert(i);
                dfs(i, nodeMap, visited);
            }
        }
        return res;
    }
    void dfs(int node, vector<vector<int>>& nodeMap,
             unordered_set<int>& visited) {
        for (int i = 0; i < nodeMap[node].size(); i++) {
            if (nodeMap[node][i] == 1 && visited.find(i) == visited.end()) {
                visited.insert(i);
                dfs(i, nodeMap, visited);
            }
        }
    }
};
// @lc code=end
