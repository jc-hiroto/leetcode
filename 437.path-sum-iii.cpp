/*
 * @lc app=leetcode id=437 lang=cpp
 *
 * [437] Path Sum III
 *
 * https://leetcode.com/problems/path-sum-iii/description/
 *
 * algorithms
 * Medium (50.15%)
 * Likes:    7896
 * Dislikes: 375
 * Total Accepted:    381K
 * Total Submissions: 762.9K
 * Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
 *
 * Given the root of a binary tree and an integer targetSum, return the number
 * of paths where the sum of the values along the path equals targetSum.
 *
 * The path does not need to start or end at the root or a leaf, but it must go
 * downwards (i.e., traveling only from parent nodes to child nodes).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
 * Output: 3
 * Explanation: The paths that sum to 8 are shown.
 *
 *
 * Example 2:
 *
 *
 * Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 1000].
 * -10^9 <= Node.val <= 10^9
 * -1000 <= targetSum <= 1000
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
   private:
    int res = 0;

   public:
    int pathSum(TreeNode* root, int targetSum) {
        dfs(root, targetSum);
        return res;
    }
    void checkPath(TreeNode* node, int target) {
        if (node == nullptr) return;
        if (node->val == target) {
            if (node->val == target) res++;
            return;
        }
        checkPath(node->left, target - node->val);
        checkPath(node->right, target - node->val);
    }
    void dfs(TreeNode* node, int target) {
        if (node == nullptr) return;
        checkPath(node, target);
        dfs(node->left, target);
        dfs(node->right, target);
    }
};
// @lc code=end
