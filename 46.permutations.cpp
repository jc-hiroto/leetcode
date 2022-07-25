/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 *
 * https://leetcode.com/problems/permutations/description/
 *
 * algorithms
 * Medium (72.22%)
 * Likes:    11820
 * Dislikes: 205
 * Total Accepted:    1.3M
 * Total Submissions: 1.7M
 * Testcase Example:  '[1,2,3]'
 *
 * Given an array nums of distinct integers, return all the possible
 * permutations. You can return the answer in any order.
 *
 *
 * Example 1:
 * Input: nums = [1,2,3]
 * Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * Example 2:
 * Input: nums = [0,1]
 * Output: [[0,1],[1,0]]
 * Example 3:
 * Input: nums = [1]
 * Output: [[1]]
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * All the integers of nums are unique.
 *
 *
 */

// @lc code=start
class Solution {
   private:
    vector<vector<int>> res;

   public:
    vector<vector<int>> permute(vector<int>& nums) {
        backtrack(0, nums);
        return res;
    }
    void backtrack(int begin, vector<int>& nums) {
        if (begin == nums.size())
            res.push_back(nums);
        else {
            for (int i = begin; i < nums.size(); i++) {
                swap(nums[begin], nums[i]);
                backtrack(begin + 1, nums);
                swap(nums[begin], nums[i]);
            }
        }
    }
};
// @lc code=end
