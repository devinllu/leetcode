#include <iostream>
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
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        vector<int> left;
        vector<int> right;
        
        traverseLeftSubtree(left, root->left);
        traverseRightSubtree(right, root->right);
        
        if (left.size() != right.size()) {
            return false;
        }
        
        for (int i = 0; i < left.size(); i++) {
            if (left[i] != right[i]) {
                return false;
            }
        }
        
        return true;
        
    }
    
    void traverseLeftSubtree(vector<int> &vec, TreeNode* root) {
        
        if (root == nullptr) {
            vec.push_back(-1);
            return;
        }
        
        vec.push_back(root->val);
        traverseLeftSubtree(vec, root->left);
        traverseLeftSubtree(vec, root->right);
    }
    
    void traverseRightSubtree(vector<int> &vec, TreeNode* root) {
        if (root == nullptr) {
            vec.push_back(-1);
            return;
        }
        
        vec.push_back(root->val);
        traverseRightSubtree(vec, root->right);
        traverseRightSubtree(vec, root->left);
    }
};