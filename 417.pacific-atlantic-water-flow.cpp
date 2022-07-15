/*
 * @lc app=leetcode id=417 lang=cpp
 *
 * [417] Pacific Atlantic Water Flow
 *
 * https://leetcode.com/problems/pacific-atlantic-water-flow/description/
 *
 * algorithms
 * Medium (49.16%)
 * Likes:    4114
 * Dislikes: 906
 * Total Accepted:    226.1K
 * Total Submissions: 447.4K
 * Testcase Example:
 * '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
 *
 * There is an m x n rectangular island that borders both the Pacific Ocean and
 * Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
 * and the Atlantic Ocean touches the island's right and bottom edges.
 *
 * The island is partitioned into a grid of square cells. You are given an m x
 * n integer matrix heights where heights[r][c] represents the height above sea
 * level of the cell at coordinate (r, c).
 *
 * The island receives a lot of rain, and the rain water can flow to
 * neighboring cells directly north, south, east, and west if the neighboring
 * cell's height is less than or equal to the current cell's height. Water can
 * flow from any cell adjacent to an ocean into the ocean.
 *
 * Return a 2D list of grid coordinates result where result[i] = [ri, ci]
 * denotes that rain water can flow from cell (ri, ci) to both the Pacific and
 * Atlantic oceans.
 *
 *
 * Example 1:
 *
 *
 * Input: heights =
 * [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
 * Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
 *
 *
 * Example 2:
 *
 *
 * Input: heights = [[2,1],[1,2]]
 * Output: [[0,0],[0,1],[1,0],[1,1]]
 *
 *
 *
 * Constraints:
 *
 *
 * m == heights.length
 * n == heights[r].length
 * 1 <= m, n <= 200
 * 0 <= heights[r][c] <= 10^5
 *
 *
 */

// @lc code=start
class Solution {
   private:
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

   public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty()) return {};
        int m = heights.size(), n = heights[0].size();
        set<pair<int, int>> pacific = {}, atlantic = {};
        vector<vector<int>> res;
        for (int i = 0; i < m; ++i) {
            dfs(heights, i, 0, pacific);
            dfs(heights, i, n - 1, atlantic);
        }
        for (int j = 0; j < n; ++j) {
            dfs(heights, 0, j, pacific);
            dfs(heights, m - 1, j, atlantic);
        }
        for (auto& p : pacific) {
            if (atlantic.count(p)) res.push_back({p.first, p.second});
        }
        return res;
    }
    void dfs(vector<vector<int>>& heights, int i, int j,
             set<pair<int, int>>& visited) {
        visited.insert({i, j});
        for (auto& dir : directions) {
            int x = i + dir.first, y = j + dir.second;
            if (x < 0 || x >= heights.size() || y < 0 || y >= heights[0].size())
                continue;
            if (heights[x][y] >= heights[i][j] &&
                visited.find({x, y}) == visited.end()) {
                dfs(heights, x, y, visited);
            }
        }
    }
};
// @lc code=end
