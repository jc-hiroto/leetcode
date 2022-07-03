/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (48.53%)
 * Likes:    34142
 * Dislikes: 1076
 * Total Accepted:    7M
 * Total Submissions: 14.4M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 *
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 *
 * You can return the answer in any order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 * Only one valid answer exists.
 *
 *
 *
 * Follow-up: Can you come up with an algorithm that is less than O(n^2) time
 * complexity?
 */

// @lc code=start
class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // int left = 0, right = nums.size() - 1;
        // vector<vector<int>> sorted;
        // for (int i = 0; i < nums.size(); i++) {
        //     sorted.push_back({nums[i], i});
        // }
        // sort(sorted.begin(), sorted.end());
        // while (left < right) {
        //     int sum = sorted[left][0] + sorted[right][0];
        //     if (sum == target) {
        //         break;
        //     } else if (sum < target) {
        //         left++;
        //     } else {
        //         right--;
        //     }
        // }
        // return {sorted[left][1], sorted[right][1]};

        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            int remain = target - nums[i];
            if (map.find(remain) != map.end()) {
                return {map[remain], i};
            } else {
                map[nums[i]] = i;
            }
        }
        return {};
    }
};
// @lc code=end
