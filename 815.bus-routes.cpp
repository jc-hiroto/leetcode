/*
 * @lc app=leetcode id=815 lang=cpp
 *
 * [815] Bus Routes
 *
 * https://leetcode.com/problems/bus-routes/description/
 *
 * algorithms
 * Hard (45.28%)
 * Likes:    2331
 * Dislikes: 58
 * Total Accepted:    94.8K
 * Total Submissions: 208.6K
 * Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
 *
 * You are given an array routes representing bus routes where routes[i] is a
 * bus route that the i^th bus repeats forever.
 *
 *
 * For example, if routes[0] = [1, 5, 7], this means that the 0^th bus travels
 * in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
 *
 *
 * You will start at the bus stop source (You are not on any bus initially),
 * and you want to go to the bus stop target. You can travel between bus stops
 * by buses only.
 *
 * Return the least number of buses you must take to travel from source to
 * target. Return -1 if it is not possible.
 *
 *
 * Example 1:
 *
 *
 * Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
 * Output: 2
 * Explanation: The best strategy is take the first bus to the bus stop 7, then
 * take the second bus to the bus stop 6.
 *
 *
 * Example 2:
 *
 *
 * Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target
 * = 12
 * Output: -1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= routes.length <= 500.
 * 1 <= routes[i].length <= 10^5
 * All the values of routes[i] are unique.
 * sum(routes[i].length) <= 10^5
 * 0 <= routes[i][j] < 10^6
 * 0 <= source, target < 10^6
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int numBusesToDestination(vector<vector<int>>& routes, int source,
                              int target) {
        unordered_map<int, vector<int>> to_routes;
        for (int i = 0; i < routes.size(); i++) {
            for (int j : routes[i]) {
                to_routes[j].push_back(i);
            }
        }
        queue<pair<int, int>> q;
        q.push({source, 0});
        unordered_set<int> visited = {source};
        while (!q.empty()) {
            int stop = q.front().first, bus = q.front().second;
            q.pop();
            if (stop == target) {
                return bus;
            }
            for (int i : to_routes[stop]) {
                for (int j : routes[i]) {
                    if (visited.find(j) == visited.end()) {
                        q.push({j, bus + 1});
                        visited.insert(j);
                    }
                }
                routes[i].clear();
            }
        }
        return -1;
    }
};
// @lc code=end