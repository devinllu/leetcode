#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) {
            return false;
        }
        
        bool res = false;
        helper(root, targetSum, 0, res);
        
        
        return res;
        
    }
    
    void helper(TreeNode* root, int target, int sum, bool &result) {
        if (root == nullptr) {
            return;
        }
        
        else if (target == sum + root->val) {
            if (root->left == nullptr && root->right == nullptr) {
                result = true;
                return;
            }
        }
        
        sum += root->val;
        
        helper(root->left, target, sum, result);
        helper(root->right, target, sum, result);
    }
};
